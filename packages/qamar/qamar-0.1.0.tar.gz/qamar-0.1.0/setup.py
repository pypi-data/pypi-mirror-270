from distutils.core import setup, Extension
import os

def main():
	src_files = ["src/" + f for f in os.listdir("src") if f.endswith(".c")]
	setup(
		name="qamar",
		version="0.1.0",
		description="A lua binding for python",
		author="Aurora Zuoris",
		author_email="programming.aurora@gmail.com",
		ext_modules=[
			Extension("qamar", src_files,include_dirs=["src"] , libraries=["lua"], extra_compile_args=["-ggdb", "-O0"], extra_link_args=["-ggdb", "-O0"])
		])

if __name__ == "__main__":
	main()
