# clip-server

This project was created with relay system idea. We want some system that can only receive, send and hold data in short time. `It's not secure at all!!` If you want to use it, please make sure you don't put sensitive data or encrypt it already.

Demo [http://clip.rop.sh](http://clip.rop.sh)

Github [https://github.com/bongtrop/clip-server](https://github.com/bongtrop/clip-server)

## Requirements

Just docker but if you want to run without docker install the below...

- Python 2 but i think that code can use in python 3
- Python module that you can see in requirements.txt
- Only linux can use i think because I use "/tmp/clip" just change it!

## Installation

If you have knowleage with docker or Ops, Dont waste the time to read this section. Do everything that you want to do.

### DockerHub

```bash
docker pull bongtrop/clip-server
```

### Docker Manual

```bash
git clone https://github.com/bongtrop/clip-server.git
cd clip-server
docker build . -t clip-server
```

### Manual

```bash
git clone https://github.com/bongtrop/clip-server.git
cd clip-server
pip install -r requirements.txt
```

## Usage

If you have knowleage with docker or Ops, Dont waste the time to read this section too. Do everything that you want to do.

### Docker

```bash
docker run -p 5000:5000  --tmpfs /tmp clip-server
```

### Without Docker

```bash
python app.py
```

## Documentation

In the application index page or you can view html in ```templates/index.html```.

## Contribution

I dont mind the way that you will contribute. Just do it. below is example.

- email
- create issue
- pull request
- carrier pigeon
- tell my friend to tell me
- foo bar

## License

Please see [LICENSE](LICENSE) file.