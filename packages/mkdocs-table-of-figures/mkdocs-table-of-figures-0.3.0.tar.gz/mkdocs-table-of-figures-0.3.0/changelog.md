# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog, and this project adheres to Semantic Versioning.

## [0.3.0] - 2024-04-29

### Added

- table column containing info abtout the type of figure
- table column containing info abtout the section where the figure is located

## [0.2.3] - 2024-04-28

### Fixed

- encoding error on file not part of the mkdocs navigation

## [0.2.2] - 2024-04-23

### Fixed

- removed the gap in the indexing jump for navigation order created by ignored elements (elements without alt text or caption)

## [0.2.1] - 2024-04-19

### Added

- options to enable/disable navigation order for the number of each figures

## [0.2.0] - 2024-04-19

### Added

- support for code blocks
- support for tables
- options to enable/disable supports for mermaid, code blocks and tables

## [0.1.7] - 2024-04-17

### Added

- specific class to mermaid figure to let user fix width if needed in `plugin.py`

## [0.1.6] - 2024-04-15

### Fixed

- print of figure in console in `plugin.py`

## [0.1.5] - 2024-04-15

### Added

- support for relative link to figures when tof file is contain in a subdirectory in `plugin.py`
- markdown="span" to support new md-in-html requirements based on mkdocs-material documentation in `plugin.py`

## [0.1.4] - 2023-06-09

### Added

- md_in_html support for relative link to image in `plugin.py`

## [0.1.3] - 2023-06-09

### Fixed

- integration of unwanted mermaid diagrams when title is empty in `plugin.py`

## [0.1.2] - 2023-06-09

### Fixed

- relative path to local image transformed to absolute path using site_url in `plugin.py`

## [0.1.1] - 2023-06-09

### Removed

- debug print of each figure in `plugin.py`

## [0.1.0] - 2023-06-09

### Added

- `readme.md`
- `plugin.py`
- Support for `Mermaid` diagrams

[0.1.4]: https://gitlab.com/cfpt-mkdocs-plugins/mkdocs-table-of-figures/-/releases/v0.1.4