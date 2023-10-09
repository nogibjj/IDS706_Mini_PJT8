"""handles cli commands"""
import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    general_query,
)


def handle_arguments(args):
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument(
        "action",
        choices=[
            "extract",
            "transform_load",
            "update_record",
            "delete_record",
            "create_record",
            "general_query",
            "read_data",
        ],
    )
    
    if args.action == "general_query":
        parser.add_argument("query")
    
    return parser.parse_args(args)


def main():
    """handles all the cli commands"""
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extract()
    elif args.action == "transform_load":
        print("Transforming data...")
        load()
    elif args.action == "general_query":
        general_query(args.query)

    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()