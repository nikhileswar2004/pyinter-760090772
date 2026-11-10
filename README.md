# Getting started

Throughout this module you will progressively build a reproducible data science project. By the end of the module your repository will contain data pipelines, tests, reports, and machine learning analyses that can be rerun automatically from source data.

This repository assumes that you are already comfortable using Python and pandas within a unit-tested framework. In this part of the module we will introduce additional tools and techniques for building reproducible data pipelines.

## Create your own repository

1. Create a new private repository using this repository as a template. Call your repository `pipeline-<STUDENT NUMBER>` replacing `<STUDENT NUMBER>` with your own student number
2. We recommend keeping this repository *private* so that your work is not visible to others.
3. Clone your repository:
```bash 
git clone <repository-url>
```
4. Change into the project directory:
```bash
cd pipeline-<STUDENT NUMBER>
```


## Creating the environment

Create the conda environment:

```bash
conda env create -f environment.yml
```


Activate the environment:

```bash
conda activate pyinter
```

Verify that everything is installed correctly:

```bash
./run check
```

## Common commands

Display available commands:

```bash
./run help
```

Run the Week 4 unit tests:

```bash
./run week4
```
 
Run the penguin DVC pipeline:

```bash
./run penguins
```

## A Note on Learning These Tools

The goal of this section of the module is not to memorise the precise syntax of tools such as Click, DVC, or Quarto. Instead, focus on understanding the problems they help us solve.

As you work through the exercises, think about questions such as:

- Why do we break an analysis into stages?
- Why do we save intermediate artefacts?
- Why do we write tests?
- Why do we make the inputs and outputs of a script explicit?

The examples in this repository are deliberately small, but the same ideas scale to much larger data science and machine learning projects.

Good luck, and take the time to understand the purpose of each tool rather than the specific implementation details of any individual script.
