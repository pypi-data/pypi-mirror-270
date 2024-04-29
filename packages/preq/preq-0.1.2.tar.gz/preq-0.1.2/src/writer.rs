use lazy_static::lazy_static;
use regex::Regex;
use std::collections::HashMap;
use std::fs::{self, File};
use std::io::Write;
use std::path::PathBuf;
use toml::Value;

lazy_static! {
    static ref DEPENDENCIES_REGEX: Regex =
        Regex::new(r"dependencies\s*=\s*\[\s*[\s\S]*?\s*\]").unwrap();
}

pub fn to_output(
    dependencies: &HashMap<String, String>,
    output: &PathBuf,
) -> Result<(), std::io::Error> {
    if output.ends_with("pyproject.toml") {
        to_pyproject(dependencies, output)
    } else {
        to_requirements(dependencies, output)
    }
}

fn to_requirements(
    requirements: &HashMap<String, String>,
    output: &PathBuf,
) -> Result<(), std::io::Error> {
    let formatted_requirements = requirements
        .into_iter()
        .map(|(k, v)| format!("{}=={}", k, v))
        .collect::<Vec<String>>()
        .join("\n");

    let mut file = File::create(output)?;
    file.write_all(formatted_requirements.as_bytes())?;
    Ok(())
}

fn to_pyproject(
    dependencies: &HashMap<String, String>,
    output: &PathBuf,
) -> Result<(), std::io::Error> {
    let contents = fs::read_to_string(output).unwrap_or_default();
    let mut toml_value = contents
        .parse::<Value>()
        .unwrap_or_else(|_| Value::Table(toml::map::Map::new()));

    let project_table = toml_value
        .as_table_mut()
        .unwrap()
        .entry("project")
        .or_insert_with(|| Value::Table(toml::map::Map::new()))
        .as_table_mut()
        .unwrap();

    let deps_array = dependencies
        .iter()
        .map(|(k, v)| Value::String(format!("{}=={}", k, v)))
        .collect::<Vec<_>>();

    // TODO: writes empty dependencies = [] if pyproject does not exist
    project_table.insert("dependencies".to_string(), Value::Array(deps_array));

    let toml_string = toml::to_string_pretty(&toml_value).unwrap();

    let mut file = File::create(output)?;
    file.write_all(toml_string.as_bytes())?;

    Ok(())
}
