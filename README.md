# PhotonSplat: 3D Scene Reconstruction and Colorization from SPAD Sensors

## ICCP 2025

### [Project Page](https://vinayak-vg.github.io/PhotonSplat/)| [arXiv Paper](https://www.arxiv.org/abs/2506.21680)

[Sai Sri Teja Kuppa](https://saisritejakuppa.github.io/) <sup>1*</sup>, 
[Sreevidya Chintalapati](https://sreevidya22.github.io/) <sup>1*</sup>, 
[Vinayak Gupta](https://vinayak-vg.github.io/) <sup>1*</sup>, 
[Mukund Varma T](https://mukundvarmat.github.io/) <sup>2</sup>, 
[Haejoon Lee](https://haejoonlee.com/) <sup>3</sup>, 
[Aswin Sankaranarayanan](https://www.ece.cmu.edu/directory/bios/sankaranarayanan-aswin.html) <sup>3</sup>, 
[Kaushik Mitra](https://www.ee.iitm.ac.in/kmitra/) <sup>1</sup>

<sup>1 </sup>Indian Institute of Technology Madras &emsp; 
<sup>1 </sup>University of California, San Diego &emsp; 
<sup>2 </sup>Carnegie Mellon University &emsp;

<sup>\*</sup> Equal Contributions.

## News

2025.07.02: We clean the code and add the README.md file.

2025.06.23: Website up and running!!!

2025.05.27: Our paper is accepted at ICCP 2025 🎉.

## Environmental Setups

Please follow the [3D-GS](https://github.com/graphdeco-inria/gaussian-splatting) to install the relative packages.

```bash
git clone https://github.com/Vinayak-VG/PhotonSplat.git
cd PhotonSplat
git submodule update --init --recursive
conda create -n ps python=3.7 
conda activate ps

pip install -r requirements.txt
pip install -e submodules/diff-gaussian-rasterization
pip install -e submodules/simple-knn
```

In our environment, we use pytorch=1.13.1+cu116.

## Dataset Preparation

Please download datasets at [here](https://github.com/Vinayak-VG/PhotonSplat/releases/download/dataset/photonscenes_dataset.zip) and unzip them to data/. Few scenes do not contain any color image while few do. For the sake of clarity, the color image is usually the last image in the set of images for each scene. We ran COLMAP for both the binary images and color images together and registered them together. Please do raise any issue if you find any problems with the dataset. 

## Usage

### Training
```bash
# For training only on binary images.
python3 -W ignore train_photon_bw.py --expname monkey_scene -s data/new_monkey --config configs real_camera_motion.txt --iteration 20000 --save_iterations 20000 --checkpoint_iterations 20000

# For training along with one color image. 
python3 -W ignore train_photon_rgb.py --expname miki_scene -s data/new_miki --config configs/real_camera_motion.txt --iteration 20000 --save_iterations 20000 --checkpoint_iterations 20000
```

### Evaluation
```bash
python3 -W ignore render.py -m outputs/miki_scene -s data/new_miki --iteration 20000
```

## BibTeX
```
@misc{teja2025photonsplat,
      title={PhotonSplat: 3D Scene Reconstruction and Colorization from SPAD Sensors}, 
      author={Kuppa Sai Sri Teja and Chintalapati Sreevidya and Gupta Vinayak et.al},
      year={2025},
      eprint={2506.21680},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

