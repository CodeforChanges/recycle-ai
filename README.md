<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="assets/logo/CodeforChanges.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Recycle Guide</h3>

   <p align="center">
    An innovative app to revolutionize recycling through technology!
    <br />
    <a href="https://github.com/CodeforChanges/recycle-ai"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/CodeforChanges/recycle-ai">View Demo</a>
    ·
    <a href="https://github.com/CodeforChanges/recycle-ai/issues">Report Bug</a>
    ·
    <a href="https://github.com/CodeforChanges/recycle-ai/issues">Request Feature</a>
  </p>
</div>

## TABLE OF CONTENTS

<details>
<summary>Title Index</summary>
<div markdown="1">
  
[1.](#1-about-the-project)  **About The Project**  
  
[2.](#2--start-guide)  **Start Guide**   
* [2-1.](#2-1--Prerequisites) Prerequisites  
* [2-2.](#2-2--Installation) Installation   
   
[3.](#3--stacks)  **Stacks**  
* [3-1.](#3-1--environment) Environment  
* [3-2.](#3-2--development)  Development  
* [3-3.](#3-3--communication)  Communication  
   
[4.](#4--how-it-works)  **How it Works**   
   
[5.](#5--env) **env**

[6.](#6--usage) **Usage**

[7.](#7--contributing) **Contributing**

[8.](#8--license) **License**

[9.](#9--contact) **Contact**

</div>
</details>

## [1.](#1-about-the-project) About The Project

In a world increasingly concerned with sustainability, the Recycle Guide app serves as a beacon of innovation. Developed with Flutter, this app not only identifies waste types through photo recognition but also educates users on proper recycling methods. It's designed to make recycling accessible and informative, encouraging environmentally friendly practices among its users.

Why Recycle Guide?

- **Educational:** Learn how to recycle different materials properly.
- **Innovative:** Utilizes photo recognition to identify waste types.
- **Community-driven:** Share and discover recycling tips within a like-minded community.
- **Informative:** Get insights on how recycled materials can be repurposed.

We're on a mission to empower individuals to make a difference in their communities through responsible waste management. Join us in making the world a cleaner, greener place.

## [2.](#2--start-guide) Start Guide

### [2-1.](#2-1--Prerequisites) Prerequisites

For building and running the application you need:

<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">

### [2-2.](#2-2--Installation) Installation

1. Clone the repo
   ```sh
   $ git clone https://github.com/CodeforChanges/recycle-ai.git
   $ cd recycle-ai
   ```
2. Install server

   ```sh
   $ python3 -m venv venv
   $ source ./venv/bin/activate
   $ pip install -U pip
   ```

   ```sh
   $ pip install -r requirements.txt
   $ pip install -e .
   ```

3. Run RabbitMQ with Docker

   ```sh
   $ docker run -d -p 5672:5672 --name rabbitmq rabbitmq
   ```

4. Run server
   ```sh
   $ export RECYCLE_AI_MQ_URL=your_mq_server_url  # amqp://guest:guest@localhost:5672/
   $ reai
   ```

## [3.](#3--stacks) Stacks

### [3-1](#3-1--environment) Environment

<img src="https://img.shields.io/badge/visual studio code-007ACC?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">

### [3-2](#3-2--development) Development

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"> <img src="https://img.shields.io/badge/rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white"> ![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFCA28?style=for-the-badge&logo=hugging%20face&logoColor=white)

### [3-3](#3-3--communication) Communication

<img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white"> <img src="https://img.shields.io/badge/googlemeet-00897B?style=for-the-badge&logo=googlemeet&logoColor=white"> <img src="https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white">

## [4.](#4--how-it-works) How it Works

```mermaid
flowchart TB
    user-->controller
    service-->RequestQueue
    RequestQueue-->PopMessageQueue
    Inference-->ResultQueue
    ResultQueue-->callback
    callback-->AiResult
    subgraph AI Inference Server
    PopMessageQueue-->Inference
    end
    subgraph RabbitMQ
    RequestQueue
    ResultQueue
    end
    subgraph API Server
    controller-->service
    callback
    end
    subgraph Database
    AiResult
    end

```

## [6](#6--usage) Usage

Recycle Guide can be used in several ways to promote recycling and sustainability:

Waste Identification: Snap a photo of your waste, and the app will tell you what type of material it is and how to recycle it properly. Community Engagement: Share your recycling achievements and tips with the community, fostering a culture of sustainability. Educational Resources: Access a wealth of information on recycling practices and the impact of recycling on the environment.

## [7](#7--contributing) Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project Create your Feature Branch (git checkout -b feature/AmazingFeature) Commit your Changes (git commit -m 'Add some AmazingFeature') Push to the Branch (git push origin feature/AmazingFeature) Open a Pull Request

## [8](#8--license) License

Distributed under the MIT License. See LICENSE.txt for more information.

## [9](#--contact) Contact

https://github.com/CodeforChanges/recycle-backend(https://github.com/CodeforChanges/recycle-backend)
