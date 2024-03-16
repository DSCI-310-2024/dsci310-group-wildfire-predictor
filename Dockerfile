FROM quay.io/jupyter/minimal-notebook

RUN conda install -y \ 
    python=3.11.8 \ 
    conda-content-trust=0.2.0 \
    conda-libmamba-solver=24.1.0 \ 
    conda==24.1.2 \ 
    jupyterlab=4.1.2 \ 
    jupyterlab-git=0.50.0 \ 
    jupyterlab-spellchecker=0.8.4 \ 
    menuinst=2.0.2 \ 
    numpy=1.26.4 \ 
    pandas=2.2.1 \ 
    pip=24.0 \  
    requests=2.31.0 \ 
    setuptools=69.1.1 \ 
    wheel=0.42.0 \ 
    matplotlib=3.8.3 \ 
    seaborn=0.13.2 \ 
    scikit-learn=1.4.1.post1 \ 
    make 