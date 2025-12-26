const path = require('path');

class FileHandler {
  constructor(dataDir = 'data') {
    this.dataDir = path.join(process.cwd(), dataDir);
  }

  async readFile(filename) {
    try {
      const fs = await import('fs').promises;
      const filePath = path.join(this.dataDir, filename);
      const data = await fs.readFile(filePath, 'utf8');
      return JSON.parse(data);
    } catch (error) {
      if (error.code === 'ENOENT') {
        return [];
      }
      throw error;
    }
  }

  async writeFile(filename, data) {
    const fs = await import('fs').promises;
    const filePath = path.join(this.dataDir, filename);
    await fs.writeFile(filePath, JSON.stringify(data, null, 2), 'utf8');
  }

  async getNextId(filename) {
    const data = await this.readFile(filename);
    if (data.length === 0) return 1;
    return Math.max(...data.map(item => item.id || 0)) + 1;
  }
}

class Wilaya {
  constructor() {
    this.fileHandler = new FileHandler();
    this.filename = 'wilayas.json';
  }

  async findAll() {
    return await this.fileHandler.readFile(this.filename);
  }

  async findById(id) {
    const wilayas = await this.findAll();
    return wilayas.find(wilaya => wilaya.id === parseInt(id));
  }

  async findByCode(code) {
    const wilayas = await this.findAll();
    return wilayas.find(wilaya => wilaya.code === code);
  }

  async create(wilayaData) {
    const wilayas = await this.findAll();
    const newWilaya = {
      id: await this.fileHandler.getNextId(this.filename),
      ...wilayaData
    };
    wilayas.push(newWilaya);
    await this.fileHandler.writeFile(this.filename, wilayas);
    return newWilaya;
  }
}

module.exports = Wilaya;