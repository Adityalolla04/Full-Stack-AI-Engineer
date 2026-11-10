# Existing practice: 21-nlp-foundations-and-vector-spaces

[Concept note](README.md) · [Your practice](practice/README.md)

These are your previously imported files, not newly generated solutions. Cell numbers below are **1-based notebook positions**, including Markdown cells; they are not execution counts.

| Material | Cells / sections | Coverage |
|---|---|---|
| [sentiment_logistic.py](practice/existing/sentiment_logistic.py) | Whole file | Toy sentiment feature/scoring example using NumPy; not a trained end-to-end model. |
| [README.md](practice/existing/original-nlp-notes.md) | Whole file | Original NLP notes preserved; see review caveats in this concept guide. |
| [Vector_spaces.py](../05-embeddings/practice/existing/Vector_spaces.py) | Whole file | Related vector-space example; stored once under Embeddings. |
| [word_embeddings.py](../05-embeddings/practice/existing/word_embeddings.py) | Whole file | Related vector-space example; stored once under Embeddings. |
| [05_NLP_Introduction.ipynb](practice/existing/05_NLP_Introduction.ipynb) | Whole file | Existing notebook moved intact, except a dataset path replacement where recorded in the migration report. |

## Before running

Run notebooks with the working directory set to the notebook's folder. Preserve the existing examples as reference and put new attempts beside them. Notebook state, package versions, external downloads, helper modules, and data requirements may still need attention. This migration does not mark topics complete.

Review caveat: the sentiment script fills positive/negative counts into the first two columns and leaves the third zero; the original notes describe a different bias/count layout. Reconcile that difference in your own practice. Cosine similarity measures vector alignment, not proof of identical meaning.

Several original course labs import absent helper modules such as `utils`, `autils`, `public_tests`, or `lab_utils_*` and reference course images/data. Those dependencies were already absent in the imported repositories. Some CV notebooks place setup cells after dependent cells. No helper implementations or reordered solutions were fabricated. See the [migration report](../../docs/MATERIAL-PLACEMENT.md).
