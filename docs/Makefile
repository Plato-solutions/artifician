# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

MARKDOWN_DIR = $(BUILDDIR)/markdown

# New target to convert RST to MD
convert-rst-to-md:
	mkdir -p $(MARKDOWN_DIR)
	for file in $(shell find . -maxdepth 1 -name '*.rst'); do \
		pandoc $$file -f rst -t markdown -o $(MARKDOWN_DIR)/$${file%.rst}.md; \
	done