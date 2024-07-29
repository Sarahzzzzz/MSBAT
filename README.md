# MSBAT (Mouse Shaking Behaviour Analysis Tool)

MSBAT is a tool for analyzing mouse behavior, with the following functionalities:
- Detecting mouse back shaking frequency
- Analyzing mouse movement trajectories
- Analyzing mouse movement speed
- Analyzing mouse back bending angles

## Environment Requirements

To use MSBAT, you need the following Python environment:

- **Python Version**: 3.7
- **Dependencies**:
  - numpy
  - pandas
  - opencv-python
  - matplotlib
  - scipy
  - scikit-learn

It is recommended to use Anaconda to manage your Python environment and dependencies. You can create a new Conda environment and install the required libraries using the following commands:

    ```bash
    conda create -n msbat python=3.7
    conda activate msbat
    conda install numpy pandas opencv-python matplotlib scipy scikit-learn
    ```

## Usage Guide

MSBAT is organized into different folders for specific analyses of DeepLabCut (DLC) generated CSV files. 

You can find the relevant tools and scripts in these folders:
1. **Analyzing Mouse Movement Trajectories**
   - **Folder**: `kc_detect`
   - **Description**: This folder includes tools for analyzing mouse movement trajectories. Refer to the documentation for instructions on how to process and analyze trajectory data.

2. **Analyzing Mouse Movement Speed**
   - **Folder**: `speed_analysis` 
   - **Description**: This folder contains scripts for calculating and analyzing mouse movement speed. Follow the instructions in the documentation to perform the analysis.

3. **Analyzing Mouse Back Bending Angles**
   - **Folder**: `v-w`
   - **Description**: This folder provides tools for analyzing the bending angles of the mouse back. Follow the steps outlined in the documentation to run the analysis.

4. **Detecting Mouse Back Shaking Frequency**
   - **Folder**: `dorsum`
   - **Description**: This folder contains scripts and tools for detecting the frequency of mouse back shaking. Follow the provided instructions and example data to run the analysis.

Note that for **Analyzing Mouse Back Bending Angles** and **Detecting Mouse Back Shaking Frequency**, you need to train a DLC model beforehand. You can find more information and download DLC from the (https://github.com/DeepLabCut/DeepLabCut).You can contact me for DeepLabCut training parameters and the entire training process.

## Contributing

If you have any suggestions or encounter issues, please submit an issue or pull request. 

## Contact

For further support or inquiries, please contact [zhangjiajia22@mails.ucas.ac.cn]
