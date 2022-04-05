from setuptools import setup, find_packages

setup(name='hk-nlp',  # 패키지 명
      version='1.0.0.9',
      description='personal package',
      author='psyche',
      author_email='hkjeon13@gmail.com',
      license='MIT',
      py_modules=['translation', 'collator', 'utils'],
      python_requires='>=3',
      install_requires=['transformers', 'datasets'],
      package_data={"hknlp":["prompt.json"]},
      packages=['hknlp']
      )
