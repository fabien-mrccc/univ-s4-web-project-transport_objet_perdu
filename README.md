# TOP - Transport Objet Perdu (French Web Application)

## Project Background
**Related Subject:** "Web Development 2023-2024"  at the University of Aix-Marseille<br>
**Team group:** GP3 <br>
**Team members:** Amina FANANI, Fabien MARCUCCINI 

## Overview
We will develop a web application that allows users to quickly retrieve the contact information of a public transportation company in the event that an item is lost while traveling. To accomplish this, we will use the following technologies that we have studied in class:
<ul>
  <li>HTML (templates);</li>
  <li>CSS;</li>
  <li>JavaScript;</li>
  <li>Flask for the server side (using Python 3);</li>
  <li>SQLite relational database.</li>
</ul>
In accordance with the MVC model, our first goal is to allow transportation companies to register on the site so that they can provide the necessary information for the application's mission. In a second phase, a user who has lost something will be able to fill in a form to select the desired transportation company in order to obtain the contact information of the relevant service.

## User Guide
<ol>
  <li>Install conda: https://docs.anaconda.com/free/miniconda/</li>
  <li>Create an environment (conda create env_name -> conda activate env_name) with:
    <ol>
      <li>Flask (conda install flask)</li>
      <li>requests (conda install requests)</li>
    </ol>
  <li>Run your flask application (flask run --debug)</li>
  <li>Use the link provided by flask in your console, for example "Running on http://127.0.0.1:5000"</li>
</ol>

## Preview
### Route "/"
<img alt="route / screenshot" src="https://fabien-marcuccini.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb09fcc6c-df16-46f2-8a4f-d37dba6294b1%2F4501e2d8-af3b-4a27-884d-c53ec9d12b0a%2F02c29fe0-61b2-49b3-a91b-dd776bee2c28.png?table=block&id=959562ff-dd90-49e8-9644-173173190c4d&spaceId=b09fcc6c-df16-46f2-8a4f-d37dba6294b1&width=1340&userId=&cache=v2" />

### Route "/inscription-compagnie-transport"
<img alt="route /inscription-compagnie-transport screenshot" src="https://fabien-marcuccini.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb09fcc6c-df16-46f2-8a4f-d37dba6294b1%2Fe6afaeb5-121f-45ea-b320-e57e2de0b31f%2FUntitled.png?table=block&id=c6c486c2-f275-4749-a2d0-a5b4e270354d&spaceId=b09fcc6c-df16-46f2-8a4f-d37dba6294b1&width=1420&userId=&cache=v2" />

### Route "/connexion-compagnie-transport"
<img alt="route /connexion-compagnie-transport" src="https://fabien-marcuccini.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb09fcc6c-df16-46f2-8a4f-d37dba6294b1%2Fafa43ed8-4f62-441f-9cea-b6c68ce9a7e4%2FUntitled.png?table=block&id=c079032b-6d8d-418e-9cc3-eb80b5ba9439&spaceId=b09fcc6c-df16-46f2-8a4f-d37dba6294b1&width=2000&userId=&cache=v2" />

### Route "/ma-compagnie-de-transport"
<img alt="route /ma-compagnie-de-transport" src="https://fabien-marcuccini.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb09fcc6c-df16-46f2-8a4f-d37dba6294b1%2F647d2fb7-672c-4dd9-a7d3-6f445a548750%2FUntitled.png?table=block&id=2bee64bd-e48a-4b9e-8f00-fbc85391e46a&spaceId=b09fcc6c-df16-46f2-8a4f-d37dba6294b1&width=2000&userId=&cache=v2" />

### Route "/recuperer-objet-perdu"
<img alt="route /recuperer-objet-perdu" src="https://fabien-marcuccini.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb09fcc6c-df16-46f2-8a4f-d37dba6294b1%2F9e0188c2-6138-49f1-a30c-2a38f7d6075b%2FUntitled.png?table=block&id=a7558ac2-4a13-4e50-8ff2-f019c70652ad&spaceId=b09fcc6c-df16-46f2-8a4f-d37dba6294b1&width=1420&userId=&cache=v2" />
<img alt="route /recuperer-objet-perdu" src="https://fabien-marcuccini.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb09fcc6c-df16-46f2-8a4f-d37dba6294b1%2Ff97abf47-5515-4996-b345-45384c093607%2FUntitled.png?table=block&id=48d6fa40-c2b3-449b-b74c-e5c45204bda2&spaceId=b09fcc6c-df16-46f2-8a4f-d37dba6294b1&width=2000&userId=&cache=v2" />



