---
layout: post
title: "삼성 갤럭시 북 + CachyOS에서 오디오가 안 나올 때 — SOF 대신 legacy HDA로 해결한 기록"
date: 2026-03-15 10:20:00 +0900
categories: [linux, troubleshooting, engineering]
tags: [Samsung, Galaxy Book, CachyOS, Arch Linux, audio, ALSA, PipeWire, SOF, HDA]
excerpt: "삼성 갤럭시 북에서 CachyOS 사용 중 내장 스피커와 이어폰 모두 소리가 나지 않던 문제를, SOF 경로 대신 legacy HDA 경로로 전환하고 ALSA 믹서를 정리해 해결한 과정 정리."
---

삼성 갤럭시 북에 CachyOS를 설치한 뒤, 오디오가 전혀 나오지 않는 문제가 있었다.

처음에는 흔히 알려진 Arch Linux 계열 해결책처럼 **SOF(Sound Open Firmware) 경로**를 강제로 쓰도록 맞췄다. 장치도 잡히고 PipeWire도 살아 있었지만, 결과적으로는 **내장 스피커도, 유선 이어폰도 둘 다 무음**이었다.

결론부터 말하면, 이 장비에서는 **SOF 경로보다 legacy HDA(`snd_hda_intel`) 경로가 맞았고**, 거기에 더해 **ALSA 믹서 상태를 정상화**하니 소리가 제대로 나왔다.

이 글은 그 과정을 나중에 다시 재현할 수 있게 남기는 기록이다.

## 증상

문제 상황은 단순했다.

- CachyOS 설치 후 시스템 전반에서 소리가 나지 않음
- PipeWire는 정상 동작
- 장치 목록에서도 오디오 카드가 보임
- 하지만 실제 재생 시 **스피커와 이어폰 모두 무음**

즉, "오디오 장치 미인식"이 아니라 **장치는 보이는데 실제 출력이 안 되는 상태**였다.

## 처음 시도했던 것: SOF 경로 강제

인터넷에서 삼성 갤럭시 북 + Arch Linux 계열 오디오 문제를 찾으면 SOF 관련 설정이 자주 보인다.
나도 처음에는 아래처럼 SOF 쪽을 강제로 쓰는 방식으로 맞춰져 있었다.

- `options snd slots=snd_soc_skl_hda_dsp`
- `blacklist snd-hda-intel`

이 상태에서는 대략 이런 식으로 보였다.

- 커널 드라이버: `sof-audio-pci-intel-tgl`
- 카드 이름: `sof-hda-dsp`
- PipeWire sink도 생성됨

겉으로 보면 멀쩡하다. 그런데 실제로는 소리가 안 났다.

여기서 중요한 포인트는, **서비스가 살아 있고 장치가 보여도 실제 아날로그 출력이 깨져 있을 수 있다**는 점이다.

## 중간에 해본 것들: 삼성 ALC298 quirk 강제

삼성 기기라서 Realtek ALC298용 quirk가 필요한가 싶어, `model=` 파라미터도 여러 개 시험했다.

시도한 후보는 아래였다.

- `alc298-samsung-amp`
- `alc298-samsung-amp-v2-2-amps`
- `alc298-samsung-amp-v2-4-amps`

처음에는 `snd-hda-codec-alc269` 쪽에 넣으려다, 로그에 아래처럼 나와서 틀린 대상이라는 것도 확인했다.

```text
snd_hda_codec_alc269: unknown parameter 'model' ignored
```

즉 `model=` 파라미터는 여기서는 `snd-hda-intel` 쪽으로 주는 게 맞았다.

그래서 수정 후 실제로는 적용되긴 했지만, **세 가지 후보 모두 효과는 없었다**.

이 단계에서 알게 된 건 하나였다.

> 이 문제는 단순한 삼성 speaker amp quirk 한 방으로 해결되는 문제가 아니었다.

## 결정적 전환: SOF를 버리고 legacy HDA로 전환

진짜 해결의 시작은 여기였다.

SOF를 포기하고, Intel 오디오를 **legacy HDA 드라이버로 강제 전환**했다.

적용한 설정은 아래 한 줄이다.

```bash
options snd-intel-dspcfg dsp_driver=1
```

내 경우 실제로는 이렇게 정리했다.

```bash
sudo tee /etc/modprobe.d/galaxybook-audio.conf >/dev/null <<'EOF'
options snd-intel-dspcfg dsp_driver=1
EOF

sudo rm -f /etc/modprobe.d/sof.conf
sudo rm -f /etc/modprobe.d/blacklist.conf
sudo reboot
```

재부팅 후 확인해보니, 드라이버가 아래처럼 바뀌었다.

- `Kernel driver in use: snd_hda_intel`
- 카드 이름: `HDA Intel PCH`
- 재생 장치: `ALC298 Analog`

이건 꽤 중요한 변화였다.

이제 문제는 "SOF 스택 문제인지 아닌지"가 아니라, **훨씬 전형적인 HDA/ALSA 출력 문제**로 좁혀졌다.

## 마지막 한 걸음: ALSA 믹서 상태 정리

legacy HDA로 바꾼 직후에도 처음에는 바로 소리가 나지 않았다.
확인해보니 믹서 상태가 이상했다.

특히 이런 식으로 잡혀 있었다.

- `Headphone`: 0%, off
- `Master`: 63%
- `Speaker`: on

즉, 드라이버 경로는 맞아졌지만 **출력 믹서 상태가 비정상적**이었다.

그래서 아래처럼 ALSA 값을 정상화했다.

```bash
amixer -c 0 sset Master 100% unmute
amixer -c 0 sset Speaker 100% unmute
amixer -c 0 sset Headphone 100% unmute
amixer -c 0 sset PCM 100%
amixer -c 0 sset 'Auto-Mute Mode' Enabled
```

이후에는:

- **내장 스피커 정상 출력**
- **유선 이어폰 정상 출력**

까지 확인했다.

즉 최종적으로는 아래 조합이 해결책이었다.

1. **SOF 대신 legacy HDA 사용**
2. **ALSA mixer 상태 정상화**

## 최종 해결 절차 요약

같은 증상이 다시 나면, 나는 아래 순서로 갈 것 같다.

### 1) legacy HDA 강제

```bash
sudo tee /etc/modprobe.d/galaxybook-audio.conf >/dev/null <<'EOF'
options snd-intel-dspcfg dsp_driver=1
EOF
```

### 2) SOF 강제 설정 제거

```bash
sudo rm -f /etc/modprobe.d/sof.conf
sudo rm -f /etc/modprobe.d/blacklist.conf
```

### 3) 재부팅

```bash
sudo reboot
```

### 4) 드라이버 확인

```bash
lspci -nnk | grep -A4 -Ei 'audio|multimedia'
aplay -l
pactl list short sinks
```

여기서 기대하는 상태는 대략 이렇다.

- `Kernel driver in use: snd_hda_intel`
- 카드 이름이 `HDA Intel PCH`
- `ALC298 Analog` 재생 장치가 보임

### 5) 믹서 상태 정리

```bash
amixer -c 0 sset Master 100% unmute
amixer -c 0 sset Speaker 100% unmute
amixer -c 0 sset Headphone 100% unmute
amixer -c 0 sset PCM 100%
amixer -c 0 sset 'Auto-Mute Mode' Enabled
```

### 6) 상태 저장

```bash
sudo alsactl store
```

## 같이 해봤지만 의미 없었던 것들

내 환경에서는 아래 시도들은 해결책이 아니었다.

- `snd-hda-intel model=alc298-samsung-amp`
- `snd-hda-intel model=alc298-samsung-amp-v2-2-amps`
- `snd-hda-intel model=alc298-samsung-amp-v2-4-amps`
- SOF 경로 유지한 채 speaker amp/EAPD 추측성 조정

장치별로 다를 수는 있겠지만, 적어도 내 갤럭시 북(Realtek ALC298, Tiger Lake-LP Smart Sound Technology Audio Controller)에서는 핵심이 아니었다.

## 왜 이게 먹혔나

정확한 내부 원인을 커널 레벨에서 단정할 수는 없지만, 관찰된 현상만 놓고 보면 꽤 명확했다.

- SOF 경로에서는 장치와 서비스는 올라왔지만 아날로그 출력이 정상적으로 동작하지 않았다.
- legacy HDA 경로로 바꾸자 `ALC298 Analog`가 보다 직접적인 형태로 잡혔다.
- 그 다음 ALSA mixer 상태를 바로잡자 실제 재생이 정상화됐다.

즉, 이 문제는 "오디오 서비스가 죽었다"기보다는,

> **이 기기에서는 SOF 경로가 실제 출력과 잘 맞지 않았고, legacy HDA + 올바른 mixer 상태가 더 잘 맞았다**

정도로 이해하는 게 가장 무난해 보인다.

## 마무리

리눅스 오디오 문제는 항상 귀찮다.
특히 장치는 멀쩡하게 보이는데 소리가 안 나면, PipeWire를 의심해야 할지, ALSA를 의심해야 할지, 커널을 의심해야 할지 감이 흐려진다.

이번 경우는 돌아보면 의외로 구조가 단순했다.

- **SOF 경로는 실패**
- **legacy HDA 경로는 성공**
- 마지막은 **믹서 상태 정리**

삼성 갤럭시 북 + CachyOS(또는 Arch 계열)에서 비슷한 증상을 겪는다면, speaker amp quirk만 계속 돌려보기보다 **`dsp_driver=1`로 먼저 legacy HDA 경로를 시험**해보는 쪽이 훨씬 빠를 수도 있다.

적어도 내 환경에서는 그랬다.
