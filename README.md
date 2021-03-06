
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<p align="center">
  
  <a href="https://github.com/usadiqgriffin/pybatch_slurm/stargazers">
  <img src="https://img.shields.io/github/stars/usadiqgriffin/pybatch_slurm?style=social">
  </a>
  <a href="https://github.com/usadiqgriffin/pybatch_slurm/network/members">
  <img src="https://img.shields.io/github/forks/usadiqgriffin/pybatch_slurm?style=social">
  </a>
  <a href="https://github.com/usadiqgriffin/pybatch_slurm/issues">
  <img src="https://img.shields.io/github/issues/usadiqgriffin/pybatch_slurm">
  </a>
  <a href="https://github.com/usadiqgriffin/pybatch_slurm/issues">
  <img src="https://img.shields.io/github/license/usadiqgriffin/pybatch_slurm  ">
  </a>                                                                    
</p>
<p align="center">
    <img width="500" height="350" src="https://s4.gifyu.com/images/Pybatch_slurm.gif">
</p>
<!-- PROJECT LOGO -->
<br />
<p align="center">

  <p align="center">
    A Python wrapper to batch process MATLAB, FSL and Freesurfer on Slurm based clusters
    <br />
    <br />
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

To get a local copy up and running follow these simple example steps.

### Prerequisites

* [Slurm workload manager](https://slurm.schedmd.com/documentation.html) <br />
To check if you have Slurm on your cluster, go to your login node and use:
```sh
  sinfo -V
  ```
* [Python 3.0](https://www.python.org/download/releases/3.0/)
  
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

### Installation

1. Log in to your slurm cluster (For UNC, this is the [longleaf cluster](https://its.unc.edu/research-computing/techdocs/getting-started-on-longleaf/#Logging%20In))
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

CD into the repo:
   ```sh
   cd pybatch_slurm
   ```
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

See the [open issues](https://github.com/usadiqgriffin/pybatch_slurm/issues) for a list of proposed features (and known issues).



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

U Sadiq - [@My LinkedIn](https://www.linkedin.com/in/usman-sadiq-765a643b/)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/all-contributors/usadiqgriffin/pybatch_slurm
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/usadiqgriffin/pybatch_slurm?style=social
[forks-url]: https://img.shields.io/github/forks/usadiqgriffin/pybatch_slurm?style=social
[stars-shield]: https://img.shields.io/github/stars/usadiqgriffin/pybatch_slurm?style=social
[stars-url]: https://github.com/usadiqgriffin/pybatch_slurm/stargazers
[issues-shield]: https://img.shields.io/github/issues/usadiqgriffin/pybatch_slurm
[issues-url]: https://github.com/usadiqgriffin/pybatch_slurm/issues
[license-shield]: https://img.shields.io/github/license/usadiqgriffin/pybatch_slurm
[license-url]: https://github.com/usadiqgriffin/pybatch_slurm/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[downloads-shield]: https://img.shields.io/github/downloads/usadiqgriffin/pybatch_slurm/total
