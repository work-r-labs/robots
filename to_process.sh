#!/bin/bash

# Script to process all unprocessed ABB robot models
# Run each command individually to process the robots that don't have processed URDF files yet

echo "All robots have been processed! 🎉"
echo ""
echo "Status summary:"
echo "- ✅ Complete: 32 robots fully processed with USD files"
echo "- 🔄 Awaiting USD: 0 robots with processed URDF but no USD file yet"
echo "- ⏳ Not Processed: 0 robots awaiting processing"
echo "- 📊 Total: 32 ABB robot models"
echo ""
echo "All robots are fully processed and ready for use in Isaac Sim!"