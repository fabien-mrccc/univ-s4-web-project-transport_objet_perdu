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

## Preview
### Route "/"
<img alt="route / screenshot" src="https://file.notion.so/f/f/b09fcc6c-df16-46f2-8a4f-d37dba6294b1/4501e2d8-af3b-4a27-884d-c53ec9d12b0a/02c29fe0-61b2-49b3-a91b-dd776bee2c28.png?id=959562ff-dd90-49e8-9644-173173190c4d&table=block&spaceId=b09fcc6c-df16-46f2-8a4f-d37dba6294b1&expirationTimestamp=1713312000000&signature=GqLSzwfQ6BZd5VO2I8hLXIiEI-97Qq1CHWcv_iy5agY&downloadName=Untitled.png" />

### Route "/inscription-compagnie-transport"
<img alt="route /inscription-compagnie-transport screenshot" src="https://file.notion.so/f/f/b09fcc6c-df16-46f2-8a4f-d37dba6294b1/e6afaeb5-121f-45ea-b320-e57e2de0b31f/Untitled.png?id=c6c486c2-f275-4749-a2d0-a5b4e270354d&table=block&spaceId=b09fcc6c-df16-46f2-8a4f-d37dba6294b1&expirationTimestamp=1713268800000&signature=lFnCw5tXOzRjvZTgxoIbCZsCJ3L7OiYdsuVqOrtGQMQ&downloadName=Untitled.png" />

### Route "/connexion-compagnie-transport"
<img alt="route /connexion-compagnie-transport" src="https://file.notion.so/f/f/b09fcc6c-df16-46f2-8a4f-d37dba6294b1/afa43ed8-4f62-441f-9cea-b6c68ce9a7e4/Untitled.png?id=c079032b-6d8d-418e-9cc3-eb80b5ba9439&table=block&spaceId=b09fcc6c-df16-46f2-8a4f-d37dba6294b1&expirationTimestamp=1713268800000&signature=abDMXwWzF_LpSfg_ICPoSNu5-Vq0B6GoCs5_k7iN6U8&downloadName=Untitled.png" />

### Route "/ma-compagnie-de-transport"
<img alt="route /ma-compagnie-de-transport" src="https://file.notion.so/f/f/b09fcc6c-df16-46f2-8a4f-d37dba6294b1/647d2fb7-672c-4dd9-a7d3-6f445a548750/Untitled.png?id=2bee64bd-e48a-4b9e-8f00-fbc85391e46a&table=block&spaceId=b09fcc6c-df16-46f2-8a4f-d37dba6294b1&expirationTimestamp=1713268800000&signature=ei3KhxF8nyzIaUYUGXPtpQ8-4HBvmZuCrw3kWmm2a3U&downloadName=Untitled.png" />

### Route "/recuperer-objet-perdu"
<img alt="route /recuperer-objet-perdu" src="https://file.notion.so/f/f/b09fcc6c-df16-46f2-8a4f-d37dba6294b1/9e0188c2-6138-49f1-a30c-2a38f7d6075b/Untitled.png?id=a7558ac2-4a13-4e50-8ff2-f019c70652ad&table=block&spaceId=b09fcc6c-df16-46f2-8a4f-d37dba6294b1&expirationTimestamp=1713268800000&signature=KVuriBLRNBHCxJ9jetInVfQYPZKrR0jC5QHIS-v1foU&downloadName=Untitled.png" />
<img alt="route /recuperer-objet-perdu" src="https://file.notion.so/f/f/b09fcc6c-df16-46f2-8a4f-d37dba6294b1/f97abf47-5515-4996-b345-45384c093607/Untitled.png?id=48d6fa40-c2b3-449b-b74c-e5c45204bda2&table=block&spaceId=b09fcc6c-df16-46f2-8a4f-d37dba6294b1&expirationTimestamp=1713268800000&signature=TIApmfV8XTZoyEY9Q3XaQxiH_yS1Ph6GP-JLqzzgE_c&downloadName=Untitled.png" />

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



