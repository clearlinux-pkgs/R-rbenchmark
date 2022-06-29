#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rbenchmark
Version  : 1.0.0
Release  : 28
URL      : https://cran.r-project.org/src/contrib/rbenchmark_1.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rbenchmark_1.0.0.tar.gz
Summary  : Benchmarking routine for R
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
is intended to facilitate benchmarking of arbitrary R code. The
        library consists of just one function, benchmark, which is a
        simple wrapper around system.time.  Given a specification of
        the benchmarking process (counts of replications, evaluation
        environment) and an arbitrary number of expressions, benchmark
        evaluates each of the expressions in the specified environment,
        replicating the evaluation as many times as specified, and
        returning the results conveniently wrapped into a data frame.

%prep
%setup -q -c -n rbenchmark
cd %{_builddir}/rbenchmark

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641088283

%install
export SOURCE_DATE_EPOCH=1641088283
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rbenchmark
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rbenchmark
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rbenchmark
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rbenchmark || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rbenchmark/DESCRIPTION
/usr/lib64/R/library/rbenchmark/INDEX
/usr/lib64/R/library/rbenchmark/Meta/Rd.rds
/usr/lib64/R/library/rbenchmark/Meta/demo.rds
/usr/lib64/R/library/rbenchmark/Meta/features.rds
/usr/lib64/R/library/rbenchmark/Meta/hsearch.rds
/usr/lib64/R/library/rbenchmark/Meta/links.rds
/usr/lib64/R/library/rbenchmark/Meta/nsInfo.rds
/usr/lib64/R/library/rbenchmark/Meta/package.rds
/usr/lib64/R/library/rbenchmark/NAMESPACE
/usr/lib64/R/library/rbenchmark/R/rbenchmark
/usr/lib64/R/library/rbenchmark/R/rbenchmark.rdb
/usr/lib64/R/library/rbenchmark/R/rbenchmark.rdx
/usr/lib64/R/library/rbenchmark/demo/benchmark.R
/usr/lib64/R/library/rbenchmark/help/AnIndex
/usr/lib64/R/library/rbenchmark/help/aliases.rds
/usr/lib64/R/library/rbenchmark/help/paths.rds
/usr/lib64/R/library/rbenchmark/help/rbenchmark.rdb
/usr/lib64/R/library/rbenchmark/help/rbenchmark.rdx
/usr/lib64/R/library/rbenchmark/html/00Index.html
/usr/lib64/R/library/rbenchmark/html/R.css
