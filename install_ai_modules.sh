# Update chat model, embedding model
rm -rf LlamaIndexChatModel
git clone https://github.com/nlp4everyone/GeneralChatEmbeddingModel.git

# Copy file
rm -rf ai_modules
cp -rf GeneralChatEmbeddingModel/chat_modules chat_modules
cp -rf GeneralChatEmbeddingModel/embedding_modules embedding_modules

cp -rf GeneralChatEmbeddingModel/config config
echo "Coping files done!"

# Install packages
pip install -r GeneralChatEmbeddingModel/requirements.txt

# Remove folder
rm -rf GeneralChatEmbeddingModel