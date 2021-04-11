

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<p align="center">
  <img width="460" height="300" src="https://s4.gifyu.com/images/Pybatch_slurm.gif">
</p>

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <p align="center">
    An amazing Python wrapper to batch process MATLAB, FSL and Freesurfer on Slurm based clusters
    <br />
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/usadiqgriffin/pybatch_slurm/issues">Report Bug</a>
    ·
    <a href="https://github.com/usadiqgriffin/pybatch_slurm/issues">Request Feature</a>
  </p>
</p>

[logo]: https://s4.gifyu.com/images/Pybatch_slurm.gif "Logo Title Text 2"

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/usadiqgriffin/pybatch_slurm/blob/main/Pybatch_slurm.png)

If you have access to a computer cluster with slurm workload manager, you have amazing computational power at your hands.  
<br />
Often times, you need to process a large number of files - hundreds or thousands - using one of the engineering/medical imaging software like MATLAB, FSL, FreeSurfer or your custom-written bash code.  
<br />
Using PySlurm, you can process all these files without much coding experience using only an excel file. PySlurm takes care of dividing your files into batches and processing your files on the cluster efficiently.   

Using PySlurm:
* You can process many files/subjects using software like MATLAB, FSL, FreeSurfer.
* You only need to have your files listed as an excel file
* If you're working in bio/biomedical engineering, your time should be spent on your problem and not learning slurm coding


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* [Slurm workload manager](https://slurm.schedmd.com/documentation.html) <br />
To check if you have Slurm on your cluster, go to your login node and use:
```sh
  sinfo -V
  ```
* [Python 3.0](https://www.python.org/download/releases/3.0/)
  

### Installation

1. Log in to your slurm cluster (For UNC, this is the longleaf cluster)
2. Clone the repo
   ```sh
   git clone https://github.com/usadiqgriffin/pybatch_slurm.git
   ```
3. Add Python module for using this repo
   ```sh
   module add python/3.8.8
   ```

<!-- USAGE EXAMPLES -->
## Usage

1. Execute simple MATLAB code on 5 subjects:
   ```sh
   module add matlab/2018a
   python pybatch_slurm.py -c "matlab matlab_print" --from 1 --to 5
   ```
2. Run [FSL's fsl_anat](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/fsl_anat) to anatomically process subjects from fsl_subs.csv:
   ```sh
   module add fsl
   python pybatch_slurm.py -c "fsl_anat -i" --from 0 --to 1 --file fsl_subs.csv
   ```
3. Run simple bash code on a subject:
   ```sh
   python pybatch_slurm.py -c "bash bash_test.sh " --from 0 --to 1 --file fsl_subs.csv
   ```
   
4. Execute MATLAB program on 5 subjects, 3 subjects per batch, waiting for 5 mins to launch the next batch:
   ```sh
   module add matlab/2018a
   python pybatch_slurm.py -c "matlab matlab_print" --from 1 --to 5 --batch 3 --time 0.08
   ```
   
5. General Usage: 
    ```
    pybatch_slurm.py [-h] -c CMD_IN [-f FILE] [--from START] [--to STOP] [--batch BATCH_SIZE] [--time TIME]
    optional arguments:
      -h, --help            show this help message and exit
      -c CMD_IN, --cmd CMD_IN
                            specify command to be run on multiple subjects
      -f FILE, --file FILE  specify csv file to load inputs/subjects from
      --from START          starting subject number
      --to STOP             last subject number
      --batch BATCH_SIZE    batch size of the files/subjects to process together
      --time TIME           how long do you expect each batch to take to process(hours)
    ```


_For help with slurm commands, please refer to the [Slurm Documentation](https://slurm.schedmd.com/)_


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b usadiqgriffin/pybatch_slurm`)
3. Commit your Changes (`git commit -m 'Add some feature to this module'`)
4. Push to the Branch (`git push origin usadiqgriffin/pybatch_slurm`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@My LinkedIn](https://www.linkedin.com/in/usman-sadiq-765a643b/) - email@example.com


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
