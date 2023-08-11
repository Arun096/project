from flask import Flask, request, render_template
import os
from PIL import Image
import shutil

app = Flask(__name__)

img = os.path.join('static','IMG\stability-sdk')
# app.config['UPLOAD'] = upload_img

origin = "D:\Python Programming\MiniProject\\"
target = 'D:\Python Programming\MiniProject\static\IMG\stability-sdk\\'
files = os.listdir(origin)

@app.route("/", methods=["GET", "POST"])
def main():
	if request.method == "POST":
		prompt = request.form.get("prompt")
		user_prompt = " ".join(prompt.split("+"))
		code = os.system(f"python -m stability_sdk.client -W 512 -H 512 \"{user_prompt}.\"")
		print(f"Command run with code {code}")
		print(user_prompt)
		for file_name in files:
			shutil.copy(origin+file_name, target+file_name)
		file = os.path.join(img, 'generation_A stunning house._1673768930_0.png')
		return render_template("main.html", userPrompt = user_prompt, image=file)
	return render_template("main.html")

if __name__ == '__main__':
	app.run()


