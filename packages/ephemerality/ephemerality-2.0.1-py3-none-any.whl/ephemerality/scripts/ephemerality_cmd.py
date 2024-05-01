import json
import sys
from argparse import ArgumentParser, Namespace
from pathlib import Path

import numpy as np
from ephemerality.src import compute_ephemerality, process_input, ProcessedData


def init_cmd_parser(parser: ArgumentParser) -> ArgumentParser:
    parser.usage = "%(prog)s [activity] [-h] [-i INPUT_FILE] [-r] [-o OUTPUT_FILE.json] [-c CORE_TYPES] [-t THRESHOLD] [--plot]..."
    parser.description = "Calculate ephemerality for a given activity vector or a set of timestamps."
    parser.add_argument(
        "-p", "--print", action="store_true",
        help="If an output file is specified, forces the results to still be printed to stdout."
    )
    parser.add_argument(
        "-i", "--input", action="store",
        help="Path to either a JSON or CSV file with input data, or to the folder with files. If not specified, "
             "will read the activity vector from the command line (as numbers delimited by either commas or spaces)."
    )
    parser.add_argument(
        "-r", "--recursive", action="store_true",
        help="Used with a folder-type input to specify to also process files in the full subfolder tree. "
             "Defaults to False."
    )
    parser.add_argument(
        "-o", "--output", action="store",
        help="Path to an output JSON file. If not specified, will output ephemerality values to stdout in JSON format."
    )
    parser.add_argument(
        "--output_indent", action="store", type=int, default=-1,
        help="Sets the indentation level of the output (either a JSON file or STDOUT) in terms of number of spaces per "
             "level. If negative, will output results as a single line. Defaults to -1."
    )
    parser.add_argument(
        "-c", "--core_types", action="store", type=str, default="lmrs",
        help="Specify core types to be computed. \"l\" for left core, \"m\" for middle core, \"r\" for right core, "
             "\"s\" for sorted core, or any combination of thereof. Default to \"lmrs\" for all 4 core types. "
    )
    parser.add_argument(
        "-t", "--threshold", action="store", type=float, default=0.8,
        help="Threshold value for ephemerality computations in case of CSV input. Defaults to 0.8."
    )
    parser.add_argument(
        "--plot", action="store_true",
        help="Visualize requested core types on the activity vector plot."
    )
    parser.add_argument(
        'activity',
        help='Activity vector (if the input file is not specified)',
        nargs='*'
    )
    parser.set_defaults(
        func=exec_cmd_compute_call
    )
    return parser


def exec_cmd_compute_call(input_args: Namespace) -> None:
    if input_args.input:
        path = Path(input_args.input)
        if path.is_dir():
            input_cases = process_input(input_folder=input_args.input, recursive=input_args.recursive)
        elif path.is_file():
            input_cases = process_input(input_file=input_args.input, threshold=float(input_args.threshold))
        else:
            raise ValueError("Unknown input file format!")
    else:
        input_cases: list[ProcessedData] = []
        if len(input_args.activity) > 1:
            input_cases.append(
                ProcessedData(
                    name="cmd-input",
                    activity=np.array(input_args.activity, dtype=float),
                    threshold=float(input_args.threshold)))
        elif len(input_args.activity) == 1:
            if ' ' in input_args.activity[0]:
                input_cases.append(
                    ProcessedData(
                        name="cmd-input",
                        activity=np.array(input_args.activity[0].split(' '), dtype=float),
                        threshold=float(input_args.threshold)))
            elif ',' in input_args.activity[0]:
                input_cases.append(
                    ProcessedData(
                        name="cmd-input",
                        activity=np.array(input_args.activity[0].split(','), dtype=float),
                        threshold=float(input_args.threshold)))
            else:
                input_cases.append(
                    ProcessedData(
                        name="cmd-input",
                        activity=np.array([input_args.activity[0]], dtype=float),
                        threshold=float(input_args.threshold)))
        else:
            sys.exit('No input provided!')

    results = {}

    for input_case in input_cases:
        results[input_case.name] = compute_ephemerality(activity_vector=input_case.activity,
                                                        threshold=input_case.threshold,
                                                        types=input_args.core_types,
                                                        plot=input_args.plot).dict()
    if len(results) == 1:
        results = results.popitem()[1]

    output_indent = input_args.output_indent if input_args.output_indent >= 0 else None
    if input_args.output:
        with open(input_args.output, 'w') as f:
            json.dump(results, f, indent=output_indent, sort_keys=True)
        if input_args.print:
            print(json.dumps(results, indent=output_indent, sort_keys=True))
        else:
            return None
    else:
        print(json.dumps(results, indent=output_indent, sort_keys=True))
