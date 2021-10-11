class Car {
  constructor(
    // Define parameters:
    brand,
    model,
    year,
    doors,
    tires,
    cooling
  ) {
    // Define properties:
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.doors = doors;
    this.equipment = {
      tires: {
        winter: tires,
        summer: tires,
      },
      cooling,
    };
  }
  // Methods:
  handleTires(winter, summer) {
    this.winter = winter;
    this.summer = summer;
  }
}

export default Car;
