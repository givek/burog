## Burog

Burog is a simple blogging platform which can be used to manage and publish content in the form of a blog. It allows users to create, organize, and publish written and visual content in a blog.

## Technologies

- Django
- Python
- HTML
- CSS
- JavaScript

## Getting Started

To get a local copy up and running follow these simple steps:

### Prerequisites

- Python 3.

  ```shell
  $ sudo apt install python3.8
  ```

### Installation

1. Create a local copy of this git repository with `git clone` command.

   ```shell
   $ git clone https://github.com/givek/burog.git
   ```

2. Create a Virtual Enviornment with the `venv` module.

   ```shell
   $ python3 -m venv venv
   ```

3. Once you’ve created a virtual environment, you may activate it.

   ```shell
   $ source venv/bin/activate
   ```

4. Now, install the requirements from the `requirements.txt` file.

   ```shell
   $ pip install -r requirements.txt
   ```

5. Now, apply the migrations with the management command.

   ```shell
   $ python manage.py migrate
   ```

6. Finally, start the developement server with the management commnad.

   ```shell
   $ python manage.py runserver
   ```

## Usage

You may use this project to publish blogs.

- Home
  ![Home](../assets/home.png)

- Profile
  ![Profile](../assets/profile.png)

- Post Detail
  ![Post Detail](../assets/post_detail.png)

- Create Post
  ![Create Post](../assets/create_post.png)

- Update Post
  ![Update Post](../assets/update_post.png)

- Register
  ![Register](../assets/register.png)

- Login
  ![Login](../assets/login.png)

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

- Vivek Gandharkar - *Initial work* - [givek](https://github.com/givek)

## License

This project is licensed under the MIT License - see the [LICENSE.md](../blob/main/LICENSE) file for details
