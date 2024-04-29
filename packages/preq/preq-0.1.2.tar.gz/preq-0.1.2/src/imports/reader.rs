use std::{
    collections::{HashMap, HashSet},
    error::Error,
    fs,
    path::{Path, PathBuf},
};

use crate::imports::parser::imports_from_file;

pub fn process_path(path: &Path) -> Result<Vec<String>, Box<dyn std::error::Error>> {
    if path.is_dir() {
        let imports = process_directory(path)?;
        Ok(imports)
    } else if path.is_file() {
        let imports = imports_from_file(path);
        Ok(imports)
    } else {
        Err(From::from(
            "The provided path is neither a file nor a directory.",
        ))
    }
}

fn process_directory(path: &Path) -> Result<Vec<String>, Box<dyn std::error::Error>> {
    let mut imports = HashSet::new();
    for entry in fs::read_dir(path)? {
        let entry = entry?;
        let path = entry.path();
        if path.is_file() && path.extension().and_then(std::ffi::OsStr::to_str) == Some("py") {
            let file_imports = imports_from_file(&path);
            imports.extend(file_imports);
        }
    }
    Ok(imports.into_iter().collect())
}

pub fn process_path_recursive(
    path: &Path,
) -> Result<HashMap<PathBuf, Vec<String>>, Box<dyn Error>> {
    let mut results = HashMap::new();
    if path.is_dir() {
        let imports = process_directory_recursive(path, &mut results)?;
        results.insert(path.to_path_buf(), imports);
    } else if path.is_file() && path.extension().and_then(std::ffi::OsStr::to_str) == Some("py") {
        let imports = imports_from_file(path);
        results.insert(path.to_path_buf(), imports);
    } else {
        return Err(From::from(
            "The provided path is neither a Python file nor a directory.",
        ));
    }
    Ok(results)
}

fn process_directory_recursive(
    directory: &Path,
    results: &mut HashMap<PathBuf, Vec<String>>,
) -> Result<Vec<String>, Box<dyn Error>> {
    let mut module_imports = HashSet::new();
    let mut has_init_py = false;

    for entry in fs::read_dir(directory)? {
        let entry = entry?;
        let path = entry.path();

        if path.is_dir() {
            let subdir_imports = process_directory_recursive(&path, results)?;
            module_imports.extend(subdir_imports);
        } else if path.is_file() {
            if path.file_name() == Some(std::ffi::OsStr::new("__init__.py")) {
                has_init_py = true;
            }
            if path.extension().and_then(std::ffi::OsStr::to_str) == Some("py") {
                let file_imports = imports_from_file(&path);
                module_imports.extend(file_imports);
            }
        }
    }

    if has_init_py {
        Ok(module_imports.into_iter().collect())
    } else {
        Ok(vec![])
    }
}
