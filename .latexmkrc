# Project-local latexmk configuration.
#
# Produces an additionally-named PDF copy after each successful build so the
# uploadable artefact is not the generic "main.pdf" that Sestoft's submission
# checklist flags. Edit OUTPUT_NAME below if a different submission filename
# is required.

my $OUTPUT_NAME = "andersen-research-project.pdf";

$success_cmd = "cp -f %D $OUTPUT_NAME";
