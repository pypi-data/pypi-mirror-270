from pyscinloopsr import before

def test_haversine():
    print("Hey2")
    # Amsterdam to Berlin
    assert before.haversine(
        4.895168, 52.370216, 13.404954, 52.520008
    ) == 576.6625818456291