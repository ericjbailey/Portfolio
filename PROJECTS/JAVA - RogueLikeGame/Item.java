import java.util.Random;

public class Item {
    private String name;
    private String type;
    private int statBonus;

    public Item(String name, String type, int statBonus) {
        this.name = name;
        this.type = type;
        this.statBonus = statBonus;
      ;
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }

    public int getStatBonus() {
        return statBonus;
    }

public static Item generateRandomItem(Random random, int level, String type) {
    // Generate random name and stat bonus based on level and type
    String name = null;
    int statBonus = 0;
    if (type.equals("weapon")) {
        String[] names = {"Sword", "Axe", "Mace", "Dagger", "Bow"};
        name = names[random.nextInt(names.length)];
        statBonus = 1 + random.nextInt(level + 1);
    } else if (type.equals("armor")) {
        String[] names = {"Leather Armor", "Chain Mail", "Plate Armor", "Robe", "Cloak"};
        name = names[random.nextInt(names.length)];
        statBonus = 1 + random.nextInt(level + 1);
    } else if (type.equals("spell")) {
        String[] names = {"Fireball", "Ice Storm", "Lightning Bolt", "Healing Touch", "Bless"};
        name = names[random.nextInt(names.length)];
        statBonus = 1 + random.nextInt(level + 1);
    }

    return new Item(name, type, statBonus);
}
    }