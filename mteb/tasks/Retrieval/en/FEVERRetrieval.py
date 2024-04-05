from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class FEVER(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="FEVER",
        dataset={
            "path": "mteb/fever",
            "revision": "bea83ef9e8fb933d90a2f1d5515737465d613e12",
        },
        description=(
            "FEVER (Fact Extraction and VERification) consists of 185,445 claims generated by altering sentences"
            " extracted from Wikipedia and subsequently verified without knowledge of the sentence they were"
            " derived from."
        ),
        reference="https://fever.ai/",
        type="Retrieval",
        category="s2p",
        eval_splits=["train", "dev", "test"],
        eval_langs=["en"],
        main_score="ndcg_at_10",
        date=None,
        form=None,
        domains=None,
        task_subtypes=None,
        license=None,
        socioeconomic_status=None,
        annotations_creators=None,
        dialect=None,
        text_creation=None,
        bibtex_citation=None,
        n_samples=None,
        avg_character_length=None,
    )