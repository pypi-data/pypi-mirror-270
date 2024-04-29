try:
    import librosa

except (OSError, ImportError):
    # This for ignoring the warning when librosa is not installed.
    # 테스트 세션에선 librosa가 꼭 설치될 필요가 없고, librosa를 설치하는 파이프라인을 추가하는게 비용이 더 들기에 아래처럼 회피합니다.
    # `sudo apt install libsndfile1-dev`를 통해 설치하세요.
    import warnings

    warnings.warn(
        "sndfile library not installed. Use `apt install libsndfile1-dev` to install it."
    )
    librosa = None
