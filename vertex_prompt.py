import vertexai
from vertexai.language_models import TextGenerationModel


def run_vertex_ai(input_user):
    vertexai.init(project="resume-auditor-394208", location="us-central1")
    parameters = {
        "temperature": 0.1,
        "max_output_tokens": 526,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
        f"""You will find power verbs for the input verb.
        Power verbs are action words that have positive meanings in English. When you use a power verb, you can communicate your message more strongly and confidently than other verbs. Power verbs are useful when writing resumes.

        input: did
        output: act
        activate
        administer
        apply
        arrange
        carry out
        conduct
        execute
        facilitate
        handle
        perform

        input: make
        output: assemble
        compose
        create
        design
        develop
        devise
        engineer
        establish
        fashion
        formulate
        generate
        produce
        synthesize

        input: fix
        output: alleviate
        amended
        debugged
        detected
        diagnosed
        investigated
        remedied
        repaired
        revitalized
        solved
        synthesized
        streamline

        input: show
        output: demonstrate
        depict
        describe
        exhibit
        highlight
        illustrate
        portray
        represent

        input: talk
        output: addressed
        advocate
        briefed
        communicate
        composed
        convince
        consulted
        collaborate
        correspond
        disseminate
        edited
        educated
        explained
        highlight
        inform
        instruct
        interact
        negotiate
        present
        publicize
        report
        specify
        verify
        welcome

        input: keep
        output: ensure
        maintain
        strengthen

        input: use
        output: operate

        input: get
        output: achieve
        obtain
        procure
        acquire

        input: change
        output: accelerate
        accomplish
        achieve
        alter
        award
        attain
        convert
        decrease
        eliminate
        expand
        excel
        generate
        heighten
        improve
        increase
        minimize
        maximize
        receive
        recognize for
        reduce
        transform

        input: help
        output: advocate
        aid
        assist
        bolster
        enhance
        enrich
        help

        input: plan
        output: administer
        commission
        develop
        evaluate
        formulate
        observe
        prepare
        research
        revise
        study
        forecast
        identify
        prioritize
        strategize

        input: {input_user}
        output:
        """,
        **parameters

    )

    return response.text
