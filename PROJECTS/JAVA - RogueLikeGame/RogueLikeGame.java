import java.util.Random;
import java.util.Scanner;

public class RogueLikeGame {
    private static final int MAX_LEVEL = 10;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        // Generate random character
        Character character = new Character(random);

        // Start game loop
        int currentLevel = 1;
        while (currentLevel <= MAX_LEVEL) {
            System.out.println("You are at level " + currentLevel);
            Enemy enemy = new Enemy(random, currentLevel);

            // Fight the enemy
            while (character.isAlive() && enemy.isAlive()) {
                System.out.println("You attack the " + enemy.getName() + "!");
                enemy.takeDamage(character.getAttackDamage());

                if (enemy.isAlive()) {
                    System.out.println("The " + enemy.getName() + " attacks you!");
                    character.takeDamage(enemy.getAttackDamage());
                }
            }

            if (character.isAlive()) {
                // Player won the fight
                System.out.println("You defeated the " + enemy.getName() + "!");
                character.gainExperience(enemy.getExperience());

                // Check if player leveled up
                if (character.getLevel() < MAX_LEVEL && character.getExperience() >= character.getExperienceNeeded()) {
                    System.out.println("Congratulations, you have leveled up to level " + (character.getLevel() + 1) + "!");
                    character.levelUp();
                }

                // Give player a random item
                Item item = Item.generateRandomItem(random, currentLevel, "armor");
                System.out.println("You found a " + item.getName() + ".");
                System.out.println("Do you want to equip it (e) or disenchant it for experience (d)?");
                String choice = scanner.nextLine();

                if (choice.equalsIgnoreCase("e")) {
                    character.equipItem(item);
                } else if (choice.equalsIgnoreCase("d")) {
                    character.gainExperience(enemy.getExperience());
                }
            } else {
                // Player lost the fight
                System.out.println("You were defeated by the " + enemy.getName() + "...");
                break;
            }

            // Choose next level
            System.out.println("Which path do you want to take, left (l) or right (r)?");
            String pathChoice = scanner.nextLine();
            if (pathChoice.equalsIgnoreCase("l")) {
                System.out.println("You take the left path.");
            } else if (pathChoice.equalsIgnoreCase("r")) {
                System.out.println("You take the right path.");
            } else {
                System.out.println("Invalid choice, defaulting to left path.");
            }

            // Move to next level
            currentLevel++;
        }

        // Game over
        if (character.isAlive()) {
            System.out.println("Congratulations, you have defeated the boss and won the game!");
        } else {
            System.out.println("Game over...");
        }
    }
}