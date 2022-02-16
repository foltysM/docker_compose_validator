<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



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
[![LinkedIn][linkedin-shield]][linkedin-url]


<div>
<h3 align="center">Simplified docker files syntax validator</h3>

  <p align="center">
    Software that checks if syntax in docker compose file provided is correct. Checks for chosen keywords using BNF. Contains of lexer and parser part.
    <br />
    <a href="https://github.com/foltysM/docker_compose_validator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/foltysM/docker_compose_validator">View Demo</a>
    ·
    <a href="https://github.com/foltysM/docker_compose_validator/issues">Report Bug</a>
    ·
    <a href="https://github.com/foltysM/docker_compose_validator/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
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
        <li><a href="#installation and usage">Installation and usage</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

After providing the input file, the lexer will search for keywords in the file using Regex. Next, parser will check the syntax. If everything will be ok, 
file structure will be shown in green color.  

![product-screenshot]

For every ile with incorrect syntax, error will be raised with short description. Moreover, the line and column of error will be indicated.

![product-screenshot2]

Above, sample console output can be seen. 



<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [bcolors](https://pypi.org/project/bcolors/)
* [re](https://docs.python.org/3/library/re.html)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is how to run the software on your PC. </br >
To get a local copy up and running follow these simple example steps.


### Installation and usage

1. Clone the repo
   ```commandline
   git clone https://github.com/foltysM/docker_compose_validator
   ```
2. Install all necessary external dependencies. This may be done using the attached requirements file.
   ```commandline
   pip install -r requirements.txt
   ```
3. Enter your input file directory and name in `main.py`
   ```python
   VIDEO_NAME = 'test2.mp4'
   ```
4. Run program

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Finding keywords in input file
- [x] Parsing tokens using BNF
- [x] Precise errors handling


See the [open issues](https://github.com/foltysM/docker_compose_validator/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/foltysM/docker_compose_validator.svg?style=for-the-badge
[contributors-url]: https://github.com/foltysM/docker_compose_validator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/foltysM/docker_compose_validator.svg?style=for-the-badge
[forks-url]: https://github.com/foltysM/docker_compose_validator/network/members
[stars-shield]: https://img.shields.io/github/stars/foltysM/docker_compose_validator.svg?style=for-the-badge
[stars-url]: https://github.com/foltysM/docker_compose_validator/stargazers
[issues-shield]: https://img.shields.io/github/issues/foltysM/docker_compose_validator.svg?style=for-the-badge
[issues-url]: https://github.com/foltysM/docker_compose_validator/issues
[license-shield]: https://img.shields.io/github/license/foltysM/docker_compose_validator.svg?style=for-the-badge
[license-url]: https://github.com/foltysM/docker_compose_validator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/michalfoltys/
[product-screenshot]: images/screenshot1.png
[product-screenshot2]: images/screenshot2.png