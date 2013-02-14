%bcond_with internet
%global packname  GenomeGraphs
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.18.0
Release:          1
Summary:          Plotting genomic information from Ensembl
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-methods R-biomaRt R-grid
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-methods R-biomaRt R-grid

%description
Genomic data analyses requires integrated visualization of known genomic
information and new experimental data.  GenomeGraphs uses the biomaRt
package to perform live annotation queries to Ensembl and translates this
to e.g. gene/transcript structures in viewports of the grid graphics
package. This results in genomic information plotted together with your
data.  Another strength of GenomeGraphs is to plot different data types
such as array CGH, gene expression, sequencing and other data, together in
one plot using the same genome coordinate system.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{with internet}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/extra
%{rlibdir}/%{packname}/help
