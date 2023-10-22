import subprocess


def compile_latex_project(tex_file_path, output_directory):
    """
    Compile a LaTeX file into a PDF using pdflatex and bibtex with a specific output directory.

    Parameters:
    - tex_file_path: Path to the .tex file to be compiled.
    - output_directory: Directory where the output files should be saved.
    """

    # Extract the base file name (without extension) to use with bibtex
    base_name = tex_file_path.rsplit('\\', 1)[-1].rsplit('.', 1)[0]

    # Run pdflatex for the first time with specified output directory
    subprocess.run(["pdflatex", "-output-directory=" +
                   output_directory, tex_file_path])

    # Run bibtex on the .aux file in the output directory
    subprocess.run(["bibtex", output_directory + "\\" + base_name + ".aux"])

    # Run pdflatex two more times with specified output directory
    subprocess.run(["pdflatex", "-output-directory=" +
                   output_directory, tex_file_path])
    subprocess.run(["pdflatex", "-output-directory=" +
                   output_directory, tex_file_path])


# Sample usage
tex_file_path = "C:\\Projects\\trabalho-conclusao-curso\\project\\LaTeX-project\\Index.tex"
output_directory = "C:\\Projects\\trabalho-conclusao-curso\\project\\LaTeX-project\\output"
compile_latex_project(tex_file_path, output_directory)
