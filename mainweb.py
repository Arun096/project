import glob
from flask import Flask, request, render_template
import os
from PIL import Image
import shutil
import glob

app = Flask(__name__)

img = os.path.join('static','IMG\stability-sdk')
# code = os.path.join('static', 'static')
# app.config['UPLOAD'] = upload_img

origin = "D:\Python Programming\MiniProject\\"
target = 'D:\Python Programming\MiniProject\static\IMG\stability-sdk\\'
t = 'static\IMG\stability-sdk\\'
files = os.listdir(origin)

file_list = []

@app.route("/", methods=["GET", "POST"])
def main():
	if request.method == "POST":
		# TODO 
		# Delete the old images in the static folder...
		# 1. Search files with .png extension in current directory
		folder_static = glob.glob(os.path.join(target, "*.png"))
		folder_temp = glob.glob(os.path.join(origin, "*.png"))
		# 2. deleting the files with png extension
		for f1 in folder_static:
			if f1 in ["D:\Python Programming\MiniProject\static\IMG\stability-sdk\menu3.png", "D:\Python Programming\MiniProject\static\IMG\stability-sdk\menu.png", "D:\Python Programming\MiniProject\static\IMG\stability-sdk\menu2.png", "D:\Python Programming\MiniProject\static\IMG\stability-sdk\2.png", "D:\Python Programming\MiniProject\static\IMG\stability-sdk\3.png"]:
				continue
			os.remove(f1)
		
		for f2 in folder_temp:
			os.remove(f2)

		i=1
		file_list = []
		prompt = request.form.get("prompt")
		user_prompt = " ".join(prompt.split("+"))
		i = 0
		while i<3: 
			code = os.system(f"python -m stability_sdk.client -W 512 -H 512 \"{user_prompt}.\"")
			print(f"Command run with code {code}")
			print(user_prompt)
			i+=1

		for file_name in glob.iglob(os.path.join(origin, "*.png")):
			new_name = str(i)+".png"
			os.rename(file_name, new_name)
			i+=1
			file_list.append(t+new_name)
			shutil.copy(new_name, target)
		return render_template("Search_field.html", userPrompt = user_prompt, image=file_list)
	return render_template("Search_field.html")

if __name__ == '__main__':
	app.run()