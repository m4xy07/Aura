# Aura

[Visit website at meetaura.me](http://meetaura.me)

[Project Working Video](https://www.youtube.com/watch?v=SqNhEiUUZtw)

Backend for Aura humanoid robot.

## Overview

Aura is a humanoid robot project that integrates various technologies to create an interactive and responsive robot. The project leverages a Raspberry Pi 5 to run a local chat machine using Ollama and TinyLLama, convert chat outcomes to voice, and display dynamic facial expressions based on responses.

## Features

- **Local Chat Machine**: Utilizes Ollama to run TinyLLama completely offline on a Raspberry Pi 5.
- **Voice Conversion**: Converts chat outcomes to voice for auditory feedback.
- **Dynamic Facial Expressions**: Changes facial expressions based on chat responses to reflect different emotions.
- **Compact Integration**: All functionalities are integrated into a Raspberry Pi 5, ensuring a compact and efficient setup.

## Setup Instructions

1. **Hardware Requirements**:

   - Raspberry Pi 5
   - Speakers for voice output
   - Display for facial expressions

2. **Software Requirements**:

   - Ollama
   - TinyLLama
   - Python (for scripting and integration)
   - Any additional libraries or dependencies required by the project

3. **Installation**:
   - Clone the repository:
     ```bash
     git clone /C:/Users/Aman/Downloads/Aura-main (1)/Aura-main
     ```
   - Navigate to the project directory:
     ```bash
     cd Aura-main
     ```
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

## Usage

1. **Running the Chat Machine**:

   - Start the local chat machine using Ollama and TinyLLama.
   - Ensure the Raspberry Pi 5 is connected to the necessary hardware (speakers and display).

2. **Interacting with Aura**:
   - Use the chat interface to interact with Aura.
   - Observe the dynamic facial expressions and listen to the voice responses.

## Project Strong Points

- Developed a local chat machine using Ollama to run TinyLLama completely offline on a Raspberry Pi 5.
- Converted chat outcomes to voice, enabling auditory feedback for responses.
- Created dynamic facial expressions for different emotions based on chat responses, enhancing user interaction.
- Utilized Raspberry Pi 5 to integrate all functionalities, ensuring a compact and efficient setup.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Team

Aura is developed by a dedicated team:

- Aman Shaikh (F-03)
- Aditya Jadhav (F-20)
- Nikhil Kurkure (F-30)
- Dheesh Medekar (F-34)

## Detailed Overview

Aura is an IoT-derived project implementing a variety of software and hardware techniques, with AI and integration tech at its core. The end result is a robot with the ability to recognize faces and detect emotions, as well as handle conversational and visual communication/display capabilities. A special feature includes the ability to respond to stimuli (digital or physical) based on app input, lending it further flexibility. Potential applications include personalization and automation industries. Future prospects such as motion, object manipulation, etc., are also considered.

### Human Faces and Expressions

TensorFlow's DeepFace library serves as the main framework for the facial recognition process. Specifically, the DeepFace function and its verify method provide the functionality. The collection and pre-storing of images from people intended for the desired database, as well as providing them in a suitable, workable manner for DeepFace, and finally displaying the results in a non-abstract, tangible manner will be largely supported by Python's open-source OpenCV library. Python's inbuilt Threading module will allow copies of the original image to be fed in for the process to work smoothly, and will throw appropriate errors based on problems in the working. Working with its Thread function also allows for the necessary safeguards between image input, detection, verification, and output. The proper frame rates for the OpenCV capture and display windows, and an extra precaution of using only 100 frames to update the result ensures a level of accuracy approaching 95%.

### Speech-to-Text and Vice Versa

The other principal input feature is detection and comprehension of speech, with appropriate output. The eSpeak library allows for a simplified and elegant implementation of this idea. Paired with compatible hardware - a file to store the text, and a microphone - it provides for single-method functionality for accessing, activating, and terminating input reception. Output text can be customized to be presented as paragraphs, or as cut-short sentences. The same text can be appended, or new text generated waiting on further input. Google’s API will be used to convert bot-generated text to speech; the impressive quality of this approach allows for lifelike speech-synthesis, enhancing user experience.

### Conversing

The Raspberry Pi 5 can be turned into a mini-GPT by running an entire LLM onto it, in our case the free-to-use Llama, importing its weights along with it. Llama’s flexibility allows it to run on multiple hardware architectures, and although using up a substantial portion of the Pi’s computing power, the seamless generation of text from text lends an impressive aspect to the machine.

### Artificial Emotions on Display

A powerful, interactive (and of course entertaining!) sub-tool of the bot includes the ability to display emotions; custom animations will be used to lend a personality of its own to Aura. The running of the animations will be featured on a 5-inch display connected with Pi’s computer, and the functionality will allow such as to display appropriate animations to the user, based on both speech and expression-image input. A default expression will also be present; the main purpose of the feature is to make any user comfortable with the interface, thus enabling extra productivity.

### Other Stimuli

Besides the aforementioned inputs, our bot will also be able to process varied physical inputs (principally touches and pats), and modify its speech/visual language accordingly. This will be accomplished with the help of sensors, and placing them at naturally expressive locations on the robot’s body (like the ‘pat-sensor’ at the top of the head) will add an extra layer of realism to the entity. These dynamic responses - combining visual, physical, and audio output - are well-supported by various distinct, separate software coming together to form a greater whole, thus justifying the project’s categorization as IoT.

### Appearance and Future Prospects

The robot’s physical manifestation will be realized via 3D-printing, and a proper color scheme will be used to highlight Aura’s functions and purpose in a visual way. The design will be oriented more towards making the bot friendly - and even sweet - in its appearance, primarily due to personal preferences as also to encourage interactions. Though presently in the theoretical realm, we express interest towards and plan to implement motion to the bot, the ability to manipulate objects to various ends, and even in formulating strategies based on ML models practically built from scratch; even more dynamic speech-to-text is also being considered, allowing for the main highlight of the bot to consider tonals, lexicals, and the like, truly marking Aura as an innovation in the area. The overall goal would be to make the bot capable of substantial multi-tasking, whilst seamlessly implementing all these functionalities in an effortless manner.
