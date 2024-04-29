use clap::Parser;

mod cli;
mod imports;
mod utils;
mod writer;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let cli = cli::Args::parse();

    let imports = imports::reader::process_path(&cli.path)?;
    let packages = imports::mapper::imports_to_packages(&imports);
    let versions = imports::mapper::packages_to_versions(&packages);
    match writer::to_output(&versions, &cli.output) {
        Ok(_) => println!("Successfully wrote requirements.txt"),
        Err(e) => eprintln!("Error writing requirements.txt: {}", e),
    }

    Ok(())
}
