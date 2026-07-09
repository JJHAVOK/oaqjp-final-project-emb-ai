from final_project.emotion_detection import emotion_detector

def test_emotion_detection():
    # Test 1: Joy
    result1 = emotion_detector("I am glad this happened")
    assert result1['dominant_emotion'] == 'joy'
    
    # Test 2: Anger
    result2 = emotion_detector("I am really mad about this")
    assert result2['dominant_emotion'] == 'anger'
    
    # Test 3: Disgust
    result3 = emotion_detector("I feel disgusted just hearing about this")
    assert result3['dominant_emotion'] == 'disgust'
    
    # Test 4: Sadness
    result4 = emotion_detector("I am so sad about this")
    assert result4['dominant_emotion'] == 'sadness'
    
    # Test 5: Fear
    result5 = emotion_detector("I am really afraid that this will happen")
    assert result5['dominant_emotion'] == 'fear'
    
    print("All tests passed!")

if __name__ == "__main__":
    test_emotion_detection()
    