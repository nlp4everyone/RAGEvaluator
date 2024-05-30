# Update chat model, embedding model
rm -rf LlamaIndexChatModel
git clone https://github.com/nlp4everyone/LlamaIndexChatModel.git

# Copy file
rm -rf ai_modules
cp -rf LlamaIndexChatModel/ai_modules ai_modules

cp -rf LlamaIndexChatModel/config config
echo "Coping files done!"

# Install packages
pip install -r LlamaIndexChatModel/requirements.txt

# Remove folder
rm -rf LlamaIndexChatModel