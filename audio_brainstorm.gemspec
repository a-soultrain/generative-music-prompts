Gem::Specification.new do |s|
  s.name        = 'audio_brainstorm'
  s.version     = '0.1.0'
  s.summary     = 'A creative partner for generating electronic music prompts.'
  s.description = 'Tailored for Ableton Live 12 Standard Edition, Novation Launchpad X, Splice, and Xfer Serum.'
  s.authors     = ['a-SoulTrain']
  s.email       = 'jgarcia1312@gmail.com'
  s.files       = ['audio_brainstorm.py']
  s.homepage    = 'https://github.com/a-soultrain/gem_drafts'
  s.license     = 'MIT'

  s.add_runtime_dependency 'nltk', '~> 3.8.1'
  s.add_runtime_dependency 'google-generativeai', '~> 0.2.0'

  s.post_install_message = <<~MESSAGE
    This gem requires NLTK data and the Google Generative AI package to function correctly.
    Additionally, please install the python-dotenv package, if you haven't already.
    Please run the following commands in your Terminal after installation:

    ```bash
    python -m nltk.downloader wordnet
    python -m nltk.downloader omw-1.4
    pip install -q -U google-generativeai
    pip install python-dotenv
    ```
  MESSAGE
end