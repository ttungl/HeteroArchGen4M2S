SUBDIRS = \
	barnes \
	cholesky \
	fft \
	fmm \
	lu \
	ocean \
	radiosity \
	radix \
	raytrace \
	water-nsquared \
	water-spatial

BENCHMARK_SUITE = m2s-benchmarks-splash2
	
TARBALL_NAME=$(BENCHMARK_SUITE).tar.gz

all:

dist: $(TARBALL_NAME)

$(TARBALL_NAME):
	rm -f $(TARBALL_NAME)
	tar -czvf $(TARBALL_NAME) --transform='s,^,$(BENCHMARK_SUITE)/,' \
		$(SUBDIRS)


