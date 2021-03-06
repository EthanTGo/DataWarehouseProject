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



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">CS 689 Data Warehouse Project</h3>

  <p align="center">
    This is CS 689 Group Project for Group 14. The following people are members of the group: Duc Nguyen, Joy Shi and Ethan Go. This Project is an implementation of a Data Stream Architecture Combined with a Data Warehouse Systems. We are using Tools such as Apache Kafka, Apache Spark and feeding the data into a Data Mart before finally processing it into a visualization tools to answer questions regarding popular foods in the Greater Boston Area.
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

For this project, we are going to perform a Stream Analysis of Twitter Data by implementing frameworks such as Apache Kafka, Apache Spark and adding it to a database and a visualization tools. Our Proof of Concepts is that of a Food Company Analyzing data about food that are found on Twitter. 

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Apache Kafka](https://kafka.apache.org/quickstart)
* [Apache Spark](https://spark.apache.org/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Before beginning, you need to register for a Twitter Developer Account since we will need to access the Twitter API. A quickstart to do this can be found at: https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api

<br />
You will need to have: Consumer Key, Consumer Secret, Access Token, Access Token Secret

### Prerequisites

There are some libraries that will need to be installed that do not come with the standard, these libraries are specified on the requirements.txt file and can be installed by running 
   ```sh
   pip install -r requirements.txt
   ```
* tweepy
* confluent_kafka
* pyspark

### Installation

1. Get API from [https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)

2. Clone the repo
   ```sh
   git clone https://github.com/EthanTGo/DataWarehouseProject
   ```
3. Install requirements.txt Python packages
   ```sh
   pip install -r requirements.txt
   ```

4. Create a file on the code folder called `config.py` and put these variables from your Twitter Developer Account in `config.py`
   ```py
      TWITTER_CONSUMER_KEY = ''
      TWITTER_CONSUMER_SECRET = ''
      TWITTER_ACCESS_TOKEN = ''
      TWITTER_ACCESS_TOKEN_SECRET = ''
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

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



<!-- CONTACT -->
## Contact

* Duc Nguyen
* Ethan Go - ethango@bu.edu
* Joy Shi 

Project Link: [https://github.com/EthanTGo/DataWarehouseProject](https://github.com/EthanTGo/DataWarehouseProject)

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
