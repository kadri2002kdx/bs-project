const fs = require('fs').promises;
const path = require('path');

class FileHandler {
  constructor(dataDir = 'data') {
    this.dataDir = path.join(__dirname, '..', '..', dataDir);
  }

  async readFile(filename) {
    try {
      const filePath = path.join(this.dataDir, filename);
      const data = await fs.readFile(filePath, 'utf8');
      return JSON.parse(data);
    } catch (error) {
      if (error.code === 'ENOENT') {
        // إذا كان الملف غير موجود، نرجع مصفوفة فارغة
        return [];
      }
      throw error;
    }
  }

  async writeFile(filename, data) {
    const filePath = path.join(this.dataDir, filename);
    await fs.writeFile(filePath, JSON.stringify(data, null, 2), 'utf8');
  }

  async getNextId(filename) {
    const data = await this.readFile(filename);
    if (data.length === 0) return 1;
    return Math.max(...data.map(item => item.id || 0)) + 1;
  }
}

module.exports = FileHandler;