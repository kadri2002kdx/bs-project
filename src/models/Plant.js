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

class Plant {
  constructor() {
    this.fileHandler = new FileHandler();
    this.filename = 'plants.json';
  }

  async findAll() {
    return await this.fileHandler.readFile(this.filename);
  }

  async findById(id) {
    const plants = await this.findAll();
    return plants.find(plant => plant.id === parseInt(id));
  }

  async create(plantData) {
    const plants = await this.findAll();
    const newPlant = {
      id: await this.fileHandler.getNextId(this.filename),
      ...plantData,
      createdAt: new Date().toISOString()
    };
    plants.push(newPlant);
    await this.fileHandler.writeFile(this.filename, plants);
    return newPlant;
  }

  async update(id, plantData) {
    const plants = await this.findAll();
    const index = plants.findIndex(plant => plant.id === parseInt(id));
    
    if (index === -1) return null;
    
    plants[index] = {
      ...plants[index],
      ...plantData,
      updatedAt: new Date().toISOString()
    };
    
    await this.fileHandler.writeFile(this.filename, plants);
    return plants[index];
  }

  async delete(id) {
    const plants = await this.findAll();
    const filteredPlants = plants.filter(plant => plant.id !== parseInt(id));
    
    if (plants.length === filteredPlants.length) return false;
    
    await this.fileHandler.writeFile(this.filename, filteredPlants);
    return true;
  }

  async findBySoilType(soilId) {
    const plants = await this.findAll();
    return plants.filter(plant => 
      plant.suitableSoils && plant.suitableSoils.includes(parseInt(soilId))
    );
  }
}

module.exports = Plant;