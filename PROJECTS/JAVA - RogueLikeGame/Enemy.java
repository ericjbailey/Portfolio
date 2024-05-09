import java.util.Random;

public class Enemy {
    private String name;
    private int health;
    private int maxHealth;
    private int attackDamage;
    private int experience;

    public Enemy(Random random, int level) {
        // Generate random name
        String[] names = {"Goblin", "Skeleton", "Zombie", "Spider", "Rat"};
        name = names[random.nextInt(names.length)];

        // Generate random stats based on level
        maxHealth = 5 + level * 2;
        health = maxHealth;
        attackDamage = 2 + level;
        experience = 10 + level * 5;
    }

    public String getName() {
        return name;
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

    public int getExperience() {
        return experience;
    }

    public void takeDamage(int damage) {
        health -= damage;
    }

    public boolean isAlive() {
        return health > 0;
    }
}