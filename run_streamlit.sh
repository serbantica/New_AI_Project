#!/bin/bash

# 🚀 AI Project Charter Tool Runner
# This script runs the Streamlit application for project planning and configuration

echo "🎯 Starting AI Project Charter Tool..."
echo "🔧 Make sure you have all dependencies installed:"
echo "   pip install -r requirements.txt"
echo ""

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit is not installed. Installing..."
    pip install streamlit pyyaml
fi

# Check if we're in the right directory
if [ ! -f "streamlit_app.py" ]; then
    echo "❌ streamlit_app.py not found. Make sure you're in the project directory."
    exit 1
fi

echo "🚀 Launching Streamlit application..."
echo "📱 The app will open in your browser at http://localhost:8502"
echo "🛑 Press Ctrl+C to stop the application"
echo ""

# Run the Streamlit app
streamlit run streamlit_app.py --server.port=8502 --server.address=0.0.0.0
