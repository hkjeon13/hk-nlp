from setuptools import setup, find_packages

setup(name='hk-nlp',  # 패키지 명
      version='1.0.2.3',
      description='personal package',
      author='psyche',
      author_email='hkjeon13@gmail.com',
      license='MIT',
      py_modules=[
            'translation', 'collator', 'utils', 'data',
            'IterableDatasetWrapper', 'SynonymReplacement',
            'spelling', 'spell_check'
      ],
      python_requires='>=3',
      install_requires=['transformers', 'datasets', 'requests'],
      package_data={"hknlp": ["data/prompt.json", "data/synonyms.json"]},
      packages=['hknlp']
      )
