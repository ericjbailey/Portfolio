import java.util.Random;

public class Character {
  private String name;
  private String race;
  private String characterClass;
  private int level;
  private int experience;
  private int experienceNeeded;
  private int health;
  private int maxHealth;
  private int attackDamage;
  private Item weapon;
  private Item armor;
  private Item spell;

  public Character(Random random) {
    // Generate random race and class
    String[] races = { "Human", "Elf", "Dwarf", "Orc" };
    String[] classes = { "Warrior", "Mage", "Rogue", "Cleric" };

    race = races[random.nextInt(races.length)];
    characterClass = classes[random.nextInt(classes.length)];

    // Generate random name based on race and class
    String[] humanNames = { "John", "Jane", "Bill", "Mary" };
    String[] elfNames = { "Legolas", "Arwen", "Galadriel", "Thranduil" };
    String[] dwarfNames = { "Gimli", "Thorin", "Dwalin", "Balin" };
    String[] orcNames = { "Grommash", "Drogath", "Mogor", "Gruumsh" };

    String[] names = null;
    if (race.equals("Human")) {
      names = humanNames;
    } else if (race.equals("Elf")) {
      names = elfNames;
    } else if (race.equals("Dwarf")) {
      names = dwarfNames;
    } else if (race.equals("Orc")) {
      names = orcNames;
    }

    name = names[random.nextInt(names.length)] + " the " + characterClass;

    // Generate random attributes based on class
    int[] attributes = new int[4];
    if (characterClass.equals("Warrior")) {
      attributes[0] = 15 + random.nextInt(6); // Strength
      attributes[1] = 10 + random.nextInt(6); // Dexterity
      attributes[2] = 10 + random.nextInt(6); // Constitution
      attributes[3] = 8 + random.nextInt(3); // Intelligence
    } else if (characterClass.equals("Mage")) {
      attributes[0] = 8 + random.nextInt(3); // Strength
      attributes[1] = 10 + random.nextInt(6); // Dexterity
      attributes[2] = 10 + random.nextInt(6); // Constitution
      attributes[3] = 15 + random.nextInt(6); // Intelligence
    } else if (characterClass.equals("Rogue")) {
      attributes[0] = 10 + random.nextInt(6); // Strength
      attributes[1] = 15 + random.nextInt(6); // Dexterity
      attributes[2] = 10 + random.nextInt(6); // Constitution
      attributes[3] = 8 + random.nextInt(3); // Intelligence
    } else if (characterClass.equals("Cleric")) {
      attributes[0] = 10 + random.nextInt(6); // Strength
      attributes[1] = 10 + random.nextInt(6); // Dexterity
      attributes[2] = 15 + random.nextInt(6); // Constitution
      attributes[3] = 8 + random.nextInt(3); // Intelligence
    }

    attackDamage = attributes[0] / 2; // Attack damage is half of Strength
    maxHealth = 10 + attributes[2] * 2; // Max health is twice the Constitution
    health = maxHealth;

    // Calculate experience needed for next level
    experienceNeeded = 10 + level * 5;

    // Give player a random starting weapon, armor, and spell
    weapon = Item.generateRandomItem(random, 1, "weapon");
    armor = Item.generateRandomItem(random, 1, "armor");
    spell = Item.generateRandomItem(random, 1, "spell");
  }

  public String getName() {
    return name;
  }

  public String getRace() {
    return race;
  }

  public String getCharacterClass() {
    return characterClass;
  }

  public int getLevel() {
    return level;
  }

  public int getExperience() {
    return experience;
  }

  public int getExperienceNeeded() {
    return experienceNeeded;
  }

  public int getHealth() {
    return health;
  }

  public int getMaxHealth() {
    return maxHealth;
  }

  public int getAttackDamage() {
    return attackDamage;
  }

  public Item getWeapon() {
    return weapon;
  }

  public Item getArmor() {
    return armor;
  }

  public Item getSpell() {
    return spell;
  }

  public void takeDamage(int damage) {
    health -= damage;
  }

  public boolean isAlive() {
    return health > 0;
  }

  public void levelUp() {
    level++;
    experience -= experienceNeeded;
    experienceNeeded = 10 + level * 5;

    // Add attribute point based on class
    if (characterClass.equals("Warrior")) {
      attackDamage += 1;
    } else if (characterClass.equals("Mage")) {
      maxHealth += 1;
    } else if (characterClass.equals("Rogue")) {
      attackDamage += 1;
    } else if (characterClass.equals("Cleric")) {
      maxHealth += 1;
    }

    // Heal to full health
    health = maxHealth;
  }

  public void gainExperience(int amount) {
    experience += amount;
  }

  public void equipItem(Item item) {
    if (item.getType().equals("weapon")) {
      if (weapon != null) {
        System.out.println("You unequip your old " + weapon.getName() + ".");
      }

      weapon = item;
      attackDamage = item.getStatBonus();
      System.out.println("You equip the " + weapon.getName() + ".");
    } else if (item.getType().equals("armor")) {
      if (armor != null) {
        System.out.println("You unequip your old " + armor.getName() + ".");
      }

      armor = item;
      maxHealth = 10 + armor.getStatBonus() * 2;
      health = Math.min(health, maxHealth);
      System.out.println("You equip the " + armor.getName() + ".");
    } else if (item.getType().equals("spell")) {
      if (spell != null) {
        System.out.println("You unequip your old " + spell.getName() + ".");
      }

      spell = item;
      System.out.println("You equip the " + spell.getName() + ".");
    }
  }
}
