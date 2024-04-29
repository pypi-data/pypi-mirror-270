use clap::{ArgAction, Parser};
use std::path::PathBuf;

#[derive(Parser, Debug)]
#[clap(
    name = "preq",
    version = "0.2.0",
    author = "atbraz",
    about = "Generates requirements.txt for Python projects.",
    long_about = "Generates requirements.txt for Python projects by parsing imports from Python files and checking for their package names and versions in your venv."
)]
pub struct Args {
    #[clap(
        value_name = "PATH",
        default_value = ".",
        help = "Input path, can be a file or a directory",
        long_help = "Input path, can be a file or a directory. If a directory is provided, all Python files in the directory will be parsed for imports.",
        required = true,
        value_parser = clap::value_parser!(PathBuf)
    )]
    pub path: PathBuf,

    #[clap(
        value_name = "OUTPUT",
        default_value = "./requirements.txt",
        short = 'o',
        long = "output",
        help = "Output file to use",
        long_help = "Output file to use. If not provided, will write to requirements.txt in the current directory. If set to 'pyproject.toml', will write to project.dependencies (must be in current directory).",
        value_parser = clap::value_parser!(PathBuf)
    )]
    pub output: PathBuf,

    #[clap(
        value_name = "TREE",
        default_value = "false",
        short = 't',
        long = "tree",
        help = "Output a tree of dependencies",
        long_help = "Output a tree of dependencies. If set to 'true', will output a tree of dependencies to the output file.",
        action = ArgAction::SetTrue,
    )]
    pub tree: bool,

    #[clap(
        value_name = "DRY_RUN",
        default_value = "false",
        long,
        help = "Dry run, do not write to file",
        long_help = "Simulates what would be written to the output file should in a regular call.",
        action = ArgAction::SetTrue,
    )]
    pub dry_run: bool,

    #[clap(
        value_name = "VERBOSE",
        short = 'v',
        long = "verbose",
        help = "Verbose mode",
        action = ArgAction::SetTrue,
    )]
    pub verbose: bool,
}
