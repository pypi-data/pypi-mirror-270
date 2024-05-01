def _generate_gapselect(answer, rest, correct_feedback, partially_correct_feedback, incorrect_feedback):
    """Generate the sections of the type of question indicated in the name of the function."""
    question = f"""
    <defaultgrade>1</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <idnumber></idnumber>
    <shuffleanswers>1</shuffleanswers>
    <correctfeedback format="html">
      <text>{correct_feedback}</text>
    </correctfeedback>
    <partiallycorrectfeedback format="html">
      <text>{partially_correct_feedback}</text>
    </partiallycorrectfeedback>
    <incorrectfeedback format="html">
      <text>{incorrect_feedback}</text>
    </incorrectfeedback>
    <shownumcorrect/>
    <selectoption>
      <text>{answer[0]}</text>
      <group>1</group>
    </selectoption>
"""
    others = ""
    for r in rest:
        others = others + f"""
    <selectoption>
      <text>{r}</text>
      <group>1</group>
    </selectoption>
"""
    res = question + others
    return(res)
