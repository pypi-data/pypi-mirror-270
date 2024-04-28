The networkx_algo_common_subtree Module
=======================================

|Pypi| |PypiDownloads| |GithubActions| |Codecov|

Networkx algorithms for maximum common ordered subtree minors (or embedding)
and maximum common subtree isomorphism. Contains pure python and cython
optimized versions.


At its core the ``maximum_common_ordered_subtree_embedding`` function is an implementation of:

.. code:: 

    Lozano, Antoni, and Gabriel Valiente.
        "On the maximum common embedded subtree problem for ordered trees."
        String Algorithmics (2004): 155-170.
        https://pdfs.semanticscholar.org/0b6e/061af02353f7d9b887f9a378be70be64d165.pdf


And ``maximum_common_ordered_subtree_isomorphism`` is a variant of the above
algorithm that returns common subtree ismorphism instead of subtree minors.


Standalone versions of code were originally submitted as PRs to networkx
proper:

https://github.com/networkx/networkx/pull/4350
https://github.com/networkx/networkx/pull/4327


These algorithms are components of algorithms in torch_liberator, see related
information:

+----------------------+------------------------------------------------------------+
| TorchLiberator       | https://gitlab.kitware.com/computer-vision/torch_liberator |
+----------------------+------------------------------------------------------------+
| Torch Hackathon 2021 | `Youtube Video`_ and `Google Slides`_                      |
+----------------------+------------------------------------------------------------+

.. _Youtube Video: https://www.youtube.com/watch?v=GQqtn61iNsc
.. _Google Slides: https://docs.google.com/presentation/d/1w9XHkPjtLRj29dw50WP0rSHRRlEfhksP_Sf8XldTSYE




.. |Pypi| image:: https://img.shields.io/pypi/v/networkx_algo_common_subtree.svg
    :target: https://pypi.python.org/pypi/networkx_algo_common_subtree

.. |PypiDownloads| image:: https://img.shields.io/pypi/dm/networkx_algo_common_subtree.svg
    :target: https://pypistats.org/packages/networkx_algo_common_subtree

.. |GithubActions| image:: https://github.com/Erotemic/networkx_algo_common_subtree/actions/workflows/tests.yml/badge.svg?branch=main
    :target: https://github.com/Erotemic/networkx_algo_common_subtree/actions?query=branch%3Amain

.. |Codecov| image:: https://codecov.io/github/Erotemic/networkx_algo_common_subtree/badge.svg?branch=main&service=github
    :target: https://codecov.io/github/Erotemic/networkx_algo_common_subtree?branch=main
