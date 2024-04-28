#!/usr/bin/env python3

import argparse
import logging
from pathlib import Path
from uploader.authentication import authenticate
from uploader.domain import TestRun
from uploader.upload import upload_test_results
from uploader.utils import regex_pattern
from uploader.zipper import find_files, zip_files

logging.basicConfig(format='%(asctime)s-%(levelname)s:%(filename)s:%(lineno)d %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def create_parser() -> argparse.ArgumentParser:
    """Parse known test runner arguments.

    Returns:
        argparse.Namespace: namespace of parsed argument values
    """
    parser = argparse.ArgumentParser(
                    prog='upload.py',
                    description='Upload test results for futher processing',
                    epilog='testpulse-io')

    parser.add_argument(
        "-tr",
        "--test-results-regex",
        required=True,
        help="Regex pattern to find test results XML files",
        type=regex_pattern,
    )

    parser.add_argument(
        "-l",
        "--localhost",
        help="For local development only",
        action='store_true'
    )

    parser.add_argument(
        "-os",
        "--operating-system",
        type=str,
        help="OS where the tests run."
    )

    parser.add_argument(
        "-lv",
        "--language-version",
        type=str,
        help="Language version. For example for Python it can be 3.11, 3.12.. For Java, 17, 21, etc.."
    )

    parser.add_argument(
        "-tfv",
        "--test-framework-version",
        type=str,
        help="Version of the test framework. For example, Pytest 8.0.0"
    )

    parser.add_argument(
        "-tt",
        "--test-type",
        type=str,
        choices=['unit', 'integration', 'e2e'],
        default='unit',
        help="Test type"
    )

    parser.add_argument(
        "-cf",
        "--config-file",
        type=str,
        help="Path to the config file."
    )

    parser.add_argument(
        "-t",
        "--token",
        type=str,
        help="Testpulse token."
    )

    return parser


def run(args: argparse.Namespace) -> None:
    root = Path().resolve()
    test_run = TestRun(args)

    logger.info('Authenticating...')
    authenticate()
    logger.info('Authenticated successfully.')

    logger.info('Finding files and zipping...')
    selected_files = find_files(test_run, root=root)
    zip_file_name = zip_files(files_list=selected_files, root=root)
    if zip_file_name is None:
        return

    logger.info(f'Saved zip file in {zip_file_name}.')

    logger.info('Uploading to our backend server...')

    link = upload_test_results(Path(zip_file_name), test_run=test_run)

    if link is not None:
        logger.info('Upload was successful. Find the test run at ' + link)


def main():
    parser = create_parser()
    args = parser.parse_args()
    run(args=args)


if __name__ == '__main__':
    main()
